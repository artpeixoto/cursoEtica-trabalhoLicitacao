import PyPDF2 as pdf
import docutils
from pathlib import Path
import sys, os

os.chdir(Path.home() / "Projeto" / "Documentos" )

path_documento_original = Path("MODELO-ATESTADO-TECNICO.pdf")
path_documento_novo =  Path("Atestado_Tecnico.pdf")
with open(path_documento_original,"rb") as documento_orig_stream, open(path_documento_novo,'wb') as  documento_novo_stream:
    documento_orig_pdf = pdf.PdfFileReader(documento_orig_stream)
    documento_novo_pdf = pdf.PdfFileWriter(documento_novo_stream)
    for pages in documento_orig_pdf.get`