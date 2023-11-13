non_fichye="fich.pdf"
def generate_pdf(non_fichye,kontni,teks):
    try:
        with open(non_fichye, "r") as f:
            b=f.read()
    except:
        with open(non_fichye, "w") as f:
            tete = "%PDF-1.5\n%\xe2\xe3\xcf\xd3\n" 
            corps = f'''
                1 0 obj
                <<
                /Type /Catalog
                /Pages 2 0 R
                /Version /1.4
                >>
                endobj

                2 0 obj
                << /Type /Pages /Kids [3 0 R] /Count 1 >>
                endobj

                3 0 obj
                <<
                /Type /Page
                /Parent 2 0 R
                /Resources << /Font << /F1 4 0 R >> >>
                /Contents 5 0 R
                /Annots [6 5 R]
                >>
                endobj

                4 0 obj
                << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
                endobj

                5 0 obj
                << /Length 55 >>
                stream
                BT
                /F1 12 Tf
                72 720 Td
                ()
                Tj
                ET
                endstream
                endobj

                6 0 obj
                << /Type /Annot /Subtype /Widget /FT /Tx
                /Rect [20 700 600 750]
                /DA (/Helv 8 Tf 0 g)
                /T (MonChampDeTexte)
                /V ({kontni})
                >>
                endobj

                trailer
                << /Root 1 0 R >>
            '''
            pieds = '\n' 
            f.write(tete) 
            f.write(corps) 
            f.write(pieds)
            print(teks)