from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_user
from app.db import create_document, update_document, add_collaborator, get_document, send_document_via_email,documents, users

# Pydantic Models
class DocumentCreateRequest(BaseModel):
    doc_id: str

class DocumentUpdateRequest(BaseModel):
    doc_id: str
    content: str

class AddCollaboratorRequest(BaseModel):
    doc_id: str
    collaborator_id: str

class ViewDocumentRequest(BaseModel):
    doc_id: str

class SendDocumentRequest(BaseModel):
    doc_id: str

# Define Router
router = APIRouter()

# Create a new document
@router.post("/document/create")
async def create_new_document(request: DocumentCreateRequest, user: dict = Depends(get_user)):
    try:
        create_document(request.doc_id, user["id"])
        return {"message": f"Document {request.doc_id} created successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Update an existing document
@router.put("/document/update")
async def update_existing_document(request: DocumentUpdateRequest, user: dict = Depends(get_user)):
    try:
        update_document(request.doc_id, request.content, user["id"])
        return {"message": f"Document {request.doc_id} updated successfully."}
    except (ValueError, PermissionError) as e:
        raise HTTPException(status_code=400, detail=str(e))

# Add a collaborator to a document
@router.post("/document/add-collaborator")
async def add_document_collaborator(request: AddCollaboratorRequest, user: dict = Depends(get_user)):
    try:
        # Periksa apakah dokumen sudah ada
        if request.doc_id not in documents:
            raise HTTPException(status_code=404, detail="Document does not exist")
        
        # Periksa apakah collaborator_id ada di database pengguna
        if request.collaborator_id not in users:
            raise HTTPException(status_code=404, detail="Collaborator does not exist")
        
        # Periksa apakah user sudah menjadi kolaborator
        if request.collaborator_id in documents[request.doc_id]["collaborators"]:
            return {"message": f"User {users[request.collaborator_id]['name']} is already a collaborator for document {request.doc_id}."}
        
        # Tambahkan kolaborator ke dokumen
        add_collaborator(request.doc_id, request.collaborator_id)
        return {"message": f"User {users[request.collaborator_id]['name']} added as a collaborator to document {request.doc_id}."}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# View a document
@router.post("/document/view")
async def view_document(request: ViewDocumentRequest, user: dict = Depends(get_user)):
    try:
        document = get_document(request.doc_id, user["id"])
        return {"document": document}
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    
# Send a document via email
@router.post("/document/send")
async def send_document(request: SendDocumentRequest, user: dict = Depends(get_user)):
    try:
        send_document_via_email(request.doc_id)
        return {"message": f"Document {request.doc_id} has been sent to all collaborators."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
