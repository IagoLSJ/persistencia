import xml.etree.ElementTree as ET
from typing import List, Optional
from schemas import LivroCreate, LivroResponse

class LivroService:
    FILE_PATH = "livros.xml"

    @staticmethod
    def _get_root():

        try:
            tree = ET.parse(LivroService.FILE_PATH)
            return tree.getroot(), tree
        except FileNotFoundError:
            root = ET.Element("livros")
            tree = ET.ElementTree(root)
            tree.write(LivroService.FILE_PATH)
            return root, tree

    @staticmethod
    def criar_livro(livro: LivroCreate) -> LivroResponse:
        root, tree = LivroService._get_root()

        for existing in root.findall("livro"):
            if int(existing.attrib["id"]) == livro.id:
                raise ValueError("O ID do livro já existe.")

        livro_element = ET.SubElement(root, "livro", id=str(livro.id))
        ET.SubElement(livro_element, "titulo").text = livro.titulo
        ET.SubElement(livro_element, "autor").text = livro.autor
        ET.SubElement(livro_element, "ano").text = str(livro.ano)
        ET.SubElement(livro_element, "genero").text = livro.genero

        tree.write(LivroService.FILE_PATH)
        return LivroResponse(**livro.dict())

    @staticmethod
    def listar_livros() -> List[LivroResponse]:
        root, _ = LivroService._get_root()
        livros = []

        for livro in root.findall("livro"):
            livros.append(
                LivroResponse(
                    id=int(livro.attrib["id"]),
                    titulo=livro.find("titulo").text,
                    autor=livro.find("autor").text,
                    ano=int(livro.find("ano").text),
                    genero=livro.find("genero").text,
                )
            )
        return livros

    @staticmethod
    def buscar_livro_por_id(livro_id: int) -> Optional[LivroResponse]:
        root, _ = LivroService._get_root()

        for livro in root.findall("livro"):
            if int(livro.attrib["id"]) == livro_id:
                return LivroResponse(
                    id=livro_id,
                    titulo=livro.find("titulo").text,
                    autor=livro.find("autor").text,
                    ano=int(livro.find("ano").text),
                    genero=livro.find("genero").text,
                )
        return None

    @staticmethod
    def atualizar_livro(livro_id: int, livro: LivroCreate) -> Optional[LivroResponse]:
        root, tree = LivroService._get_root()

        for livro_element in root.findall("livro"):
            if int(livro_element.attrib["id"]) == livro_id:
                livro_element.find("titulo").text = livro.titulo
                livro_element.find("autor").text = livro.autor
                livro_element.find("ano").text = str(livro.ano)
                livro_element.find("genero").text = livro.genero
                tree.write(LivroService.FILE_PATH)
                return LivroResponse(**livro.dict())
        return None

    @staticmethod
    def deletar_livro(livro_id: int) -> bool:
        root, tree = LivroService._get_root()

        for livro_element in root.findall("livro"):
            if int(livro_element.attrib["id"]) == livro_id:
                root.remove(livro_element)
                tree.write(LivroService.FILE_PATH)
                return True
        return False
