from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
pdf.image('files/tiger.jpeg', w=80, h=50)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Royal Bengal Tiger", align='C', border=1, ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=0, h=20, txt="Description", ln=1)

pdf.set_font(family='Times', style='B', size=12)
para1 = """
The Bengal tiger is a population of the Panthera tigris tigris subspecies and the nominate tiger subspecies.[1] It ranks among the biggest wild cats alive today.[2][3] It is considered to belong to the world's charismatic megafauna.[4]

The tiger is estimated to have been present in the Indian subcontinent since the Late Pleistocene, for about 12,000 to 16,500 years.[5][6][7] Today, it is threatened by poaching, loss and fragmentation of habitat, and was estimated at comprising fewer than 2,500 wild individuals by 2011. None of the Tiger Conservation Landscapes within its range is considered large enough to support an effective population of more than 250 adult individuals.
"""
pdf.multi_cell(w=0, h=20, txt=para1)

pdf.output('files/output.pdf')
