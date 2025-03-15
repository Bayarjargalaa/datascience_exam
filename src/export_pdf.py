from fpdf import FPDF

# PDF үүсгэх
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Тайлан унших
with open("reports/summary_report.txt", "r", encoding="utf-8") as f:
    for line in f:
        clean_line = line.encode("latin-1", "ignore").decode("latin-1")  
        pdf.cell(200, 10, txt=clean_line, ln=True)

# PDF хадгалах
pdf.output("reports/final_report.pdf", "F")

print("PDF тайлан амжилттай хадгалагдлаа!")
