from weasyprint import HTML

class PdfGeneratorService:
    def __init__(self, target: str) -> None:
        self.target = target

    def generate_pdf(self, htmlStructure: str) -> None:
        HTML(string=f"<p>{htmlStructure}</p>").write_pdf(self.target, pdf_variant="pdf/a-3u")