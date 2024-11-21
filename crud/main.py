from fastapi import FastAPI, HTTPException
from schemas import LivroCreate, LivroResponse
from service import LivroService
from typing import List

app = FastAPI()

@app.post("/livros", response_model=LivroResponse)
async def criar_livro(livro: LivroCreate):
    try:
        return LivroService.criar_livro(livro)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/livros", response_model=List[LivroResponse])
async def listar_livros():
    return LivroService.listar_livros()

@app.get("/livros/{livro_id}", response_model=LivroResponse)
async def buscar_livro_por_id(livro_id: int):
    livro = LivroService.buscar_livro_por_id(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@app.put("/livros/{livro_id}", response_model=LivroResponse)
async def atualizar_livro(livro_id: int, livro: LivroCreate):
    livro_atualizado = LivroService.atualizar_livro(livro_id, livro)
    if not livro_atualizado:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro_atualizado

@app.delete("/livros/{livro_id}")
async def deletar_livro(livro_id: int):
    if not LivroService.deletar_livro(livro_id):
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return {"message": "Livro deletado com sucesso"}
