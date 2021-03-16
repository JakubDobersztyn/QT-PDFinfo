from PyPDF2 import PdfFileReader

rolls = [210, 297, 420, 594, 841, 914]
roll_dict = {}

def pdf_size_calc(list):
    for roll in rolls[1:]:
        roll_dict[roll] = 0
    summ_sqr = 0
    summ_a4 = 0
    summ_a3 = 0
    summ_sqra3 = 0
    summ_wf = 0
    for file in list:
        pdf = PdfFileReader(open(file, 'rb'))
        number_of_pages = pdf.getNumPages()
        for page_number in range(number_of_pages):
            page = pdf.getPage(page_number)
            # a_size = (float(page['/MediaBox'][3]) * 0.3527777778) / 1000
            # b_size = (float(page['/MediaBox'][2]) * 0.3527777778) / 1000
            a_size = float(page.mediaBox.getWidth()) * 0.3527777778 / 1000
            b_size = float(page.mediaBox.getHeight()) * 0.3527777778 / 1000
            a_size, b_size = rolls_valid(a_size,b_size)
            if (0.278 < a_size < 0.303 and 0.2 < b_size < 0.217) or (0.278 < b_size < 0.303 and 0.2 < a_size < 0.217):
                summ_a4 += 1
            elif (0.278 < a_size < 0.303 and 0.41 < b_size < 0.433) or (
                    0.278 < b_size < 0.303 and 0.41 < a_size < 0.433):
                summ_a3 += 1
                sqr = a_size * b_size
                summ_sqra3 += sqr
            else:
                sqr = a_size * b_size
                summ_sqr += sqr
                summ_wf += 1

    return summ_a4, summ_a3, ("{:.4f}".format(summ_sqra3)), ("{:.4f}".format(summ_sqr)), summ_wf, roll_count_str(summ_a3)


def roll_count_str(a3):
    roll_str = ""
    roll_dict[420] -= a3
    for i in roll_dict:
        if roll_dict[i] != 0:
            roll_str += f"Rolek {i}:    {roll_dict[i]}\n"

    return roll_str


def rolls_valid(size_a, size_b):
    valid_a = False
    valid_b = False
    for i in range(len(rolls)):
        roll = rolls[i] / 1000 + 0.006
        if valid_a: break
        if i < (len(rolls) - 1):
            if roll < size_a < (float(rolls[i + 1]) / 1000):
                valid_a = rolls[i + 1] / 1000
                diff_valid_a = valid_a - size_a
        else:
            if not valid_a:
                valid_a = size_a
                diff_valid_a = 1000
    for i in range(len(rolls)):
        roll = rolls[i] / 1000 + 0.006
        if valid_b: break
        if i < (len(rolls) - 1):
            if roll < size_b < (float(rolls[i + 1]) / 1000):
                valid_b = rolls[i + 1] / 1000
                diff_valid_b = valid_b - size_b
                break
        else:
            if not valid_b:
                valid_b = size_b
                diff_valid_b = 10000000000
    if diff_valid_a < diff_valid_b:
        dictvalue = int(round(valid_a*1000, 0))
        if dictvalue != 210: roll_dict[dictvalue] += 1
        return valid_a, size_b
    dictvalue = int(round(valid_b*1000, 0))
    if dictvalue != 210: roll_dict[dictvalue] += 1
    return size_a, valid_b

#
# a = 0.450
# b = 0.8
# print('\n', rolls_valid(a, b))

# lst = ['/media/croni/workspace/QT_pdfinfo/test_pdfs/blabla/a3.pdf',
#        '/media/croni/workspace/QT_pdfinfo/test_pdfs/blabla/a0.pdf',
#        '/media/croni/workspace/QT_pdfinfo/test_pdfs/blabla/a2.pdf',
#        '/media/croni/workspace/QT_pdfinfo/test_pdfs/blabla/a4.pdf']
# a, b, c, d = pdf_size_calc(lst)
# print(f"Ilosc a4: {a} \nIlosc a3: {b} metry a3: {c} \nmetry: {d}")
