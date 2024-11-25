# db.py

api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
    "5f0c7127-3be9-4488-b801-c7b6415b45e9": "mUP7PpTHmFAkxcQLWKMY8t"
}

users = {
    "7oDYjo3d9r58EJKYi5x4E8": {
        "name": "Arvyno",
        "email": "arvyno@example.com"
    },
    "mUP7PpTHmFAkxcQLWKMY8t": {
        "name": "Bastian",
        "email": "bastian@example.com"
    },
}

# Data dokumen disimpan di sini, di mana setiap dokumen memiliki ID, konten, dan daftar kolaborator.
documents = {}

def check_api_key(api_key: str):
    return api_key in api_keys

def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]

def create_document(doc_id, owner_id):
    if doc_id in documents:
        raise ValueError("Document ID already exists")
    documents[doc_id] = {"content": "", "collaborators": [owner_id]}

def update_document(doc_id, content, user_id):
    if doc_id not in documents:
        raise ValueError("Document does not exist")
    if user_id not in documents[doc_id]["collaborators"]:
        raise PermissionError("User not authorized to edit this document")
    documents[doc_id]["content"] = content

def add_collaborator(doc_id, user_id):
    if doc_id not in documents:
        raise ValueError("Document does not exist")
    if user_id in documents[doc_id]["collaborators"]:
        raise ValueError("User is already a collaborator")
    documents[doc_id]["collaborators"].append(user_id)

def get_document(doc_id, user_id):
    if doc_id not in documents or user_id not in documents[doc_id]["collaborators"]:
        raise PermissionError("User not authorized to access this document")
    return documents[doc_id]

def send_document_via_email(doc_id):
    doc = documents[doc_id]
    for collaborator_id in doc["collaborators"]:
        user = users[collaborator_id]
        print(f"Sending document '{doc_id}' to {user['email']}")
