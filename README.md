# TubesTST API Documentation

This documentation provides instructions for using the API endpoints available in the TubesTST project. The API allows authenticated users to create, update, manage, and collaborate on documents.

---

## **Base URL**

https://tubestst-production.up.railway.app/

---

## **Authentication**

The API uses **API Key Authentication**. Include a valid API key in the `Authorization` header for all protected routes:

Authorization: Bearer <API_KEY>

Predefined API keys for testing:

| **API Key**                              | **User Name** | **Email**             |
|------------------------------------------|---------------|-----------------------|
| `e54d4431-5dab-474e-b71a-0db1fcb9e659`  | Arvyno        | arvyno@example.com    |
| `5f0c7127-3be9-4488-b801-c7b6415b45e9`  | Bastian       | bastian@example.com   |

---

## **Endpoint List**

### **1. Create a New Document**
- **Path**: `/api/v1/secure/document/create`
- **Method**: `POST`
- **Description**: Creates a new document owned by the authenticated user.

**Headers**:
Authorization: Bearer <API_KEY> Content-Type: application/json


**Body**:
```json
{
  "doc_id": "string"
}

Responses:

Success:
{
  "message": "Document doc123 created successfully."
}

Error (400):
{
  "detail": "Document ID already exists"
}


2. Update an Existing Document
Path: /api/v1/secure/document/update
Method: PUT
Description: Updates the content of an existing document.
Headers:
Authorization: Bearer <API_KEY>
Content-Type: application/json

Body:
{
  "doc_id": "string",
  "content": "string"
}

Responses:

Success:
{
  "message": "Document doc123 updated successfully."
}

Error (400):
{
  "detail": "User not authorized to edit this document"
}


3. Add a Collaborator to a Document
Path: /api/v1/secure/document/add-collaborator
Method: POST
Description: Adds a collaborator to an existing document.
Headers:
Authorization: Bearer <API_KEY>
Content-Type: application/json

Body:
{
  "doc_id": "string",
  "collaborator_id": "string"
}

Responses:

Success:
{
  "message": "User Bastian added as a collaborator to document doc123."
}

Error (404):
{
  "detail": "Document does not exist"
}

Error (400):
{
  "message": "User Bastian is already a collaborator for document doc123."
}


4. View a Document
Path: /api/v1/secure/document/view
Method: POST
Description: Views the content of a document if the user is authorized.
Headers:
Authorization: Bearer <API_KEY>
Content-Type: application/json

Body:
{
  "doc_id": "string"
}

Responses:

Success:
{
  "document": {
    "content": "Document content here",
    "collaborators": ["collaborator_id1", "collaborator_id2"]
  }
}

Error (403):
{
  "detail": "User not authorized to access this document"
}


5. Send a Document via Email
Path: /api/v1/secure/document/send
Method: POST
Description: Sends the document to all collaborators via email.
Headers:
Authorization: Bearer <API_KEY>
Content-Type: application/json

Body:
{
  "doc_id": "string"
}

Responses:

Success:
{
  "message": "Document doc123 has been sent to all collaborators."
}

Error(400):
{
  "detail": "Document does not exist"
}


Examples
Using cURL
1. Create a New Document
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/create" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123"}'

2. Update a Document
curl -X PUT "https://tubestst-production.up.railway.app/api/v1/secure/document/update" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123", "content": "Updated content"}'

3. Add a Collaborator
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/add-collaborator" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123", "collaborator_id": "mUP7PpTHmFAkxcQLWKMY8t"}'

4. View a document
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/view" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123"}'

5. Send a document via Email
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/send" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123"}'


Notes
Ensure doc_id values are unique for new documents.
Collaborators must have valid user IDs.
Use the predefined API keys for testing.

Contact
For any issues or inquiries, please contact the project owner.
