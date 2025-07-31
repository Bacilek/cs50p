from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 32)
        self.cell(80)  # cursor to the right
        self.cell(30, 10, "CS50 Shirtificate", align="C")  # print in x=30mm, y=10mm, align to center
        self.ln(150)  # \n


def main():
    pdf = PDF()  # instantiate
    pdf.add_page()
    pdf.image("shirtificate.png", 10, 107.1, pdf.epw)
    name = input ("Name: ")
    pdf.set_text_color(255)  # white
    pdf.set_font("helvetica", "B", 16)  # bold
    pdf.cell(90)
    pdf.cell(15, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
