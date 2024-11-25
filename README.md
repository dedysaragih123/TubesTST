TubesTST API Documentation
This documentation provides instructions for using the following API endpoints:

Create a New Document
Update an Existing Document
Add a Collaborator to a Document
View a Document
Send a Document via Email
Base URL
arduino
Copy code
https://tubestst-production.up.railway.app/
Authentication
The API uses API Key Authentication. Include a valid API key in the Authorization header for all protected routes:

http
Copy code
Authorization: Bearer <API_KEY>
Predefined API keys:

API Key	User Name	Email
e54d4431-5dab-474e-b71a-0db1fcb9e659	Arvyno	arvyno@example.com
5f0c7127-3be9-4488-b801-c7b6415b45e9	Bastian	bastian@example.com
Endpoint List
1. Create a New Document
Path: /api/v1/secure/document/create
Method: POST
Description: Creates a new document owned by the authenticated user.
Headers:

http
Copy code
Authorization: Bearer <API_KEY>
Content-Type: application/json
Body Parameters:

json
Copy code
{
  "doc_id": "string"
}
Responses:

Success:
json
Copy code
{
  "message": "Document doc123 created successfully."
}
Error:
400 Bad Request: Document ID already exists.
json
Copy code
{
  "detail": "Document ID already exists"
}
2. Update an Existing Document
Path: /api/v1/secure/document/update
Method: PUT
Description: Updates the content of an existing document.
Headers:

http
Copy code
Authorization: Bearer <API_KEY>
Content-Type: application/json
Body Parameters:

json
Copy code
{
  "doc_id": "string",
  "content": "string"
}
Responses:

Success:
json
Copy code
{
  "message": "Document doc123 updated successfully."
}
Error:
400 Bad Request: Document does not exist or user is not authorized.
json
Copy code
{
  "detail": "User not authorized to edit this document"
}
3. Add a Collaborator to a Document
Path: /api/v1/secure/document/add-collaborator
Method: POST
Description: Adds a collaborator to an existing document.
Headers:

http
Copy code
Authorization: Bearer <API_KEY>
Content-Type: application/json
Body Parameters:

json
Copy code
{
  "doc_id": "string",
  "collaborator_id": "string"
}
Responses:

Success:
json
Copy code
{
  "message": "User Bastian added as a collaborator to document doc123."
}
Error:
404 Not Found: Document or collaborator does not exist.
json
Copy code
{
  "detail": "Document does not exist"
}
400 Bad Request: Collaborator is already added.
json
Copy code
{
  "message": "User Bastian is already a collaborator for document doc123."
}
4. View a Document
Path: /api/v1/secure/document/view
Method: POST
Description: Views the content of a document if the user is authorized.
Headers:

http
Copy code
Authorization: Bearer <API_KEY>
Content-Type: application/json
Body Parameters:

json
Copy code
{
  "doc_id": "string"
}
Responses:

Success:
json
Copy code
{
  "document": {
    "content": "Document content here",
    "collaborators": ["collaborator_id1", "collaborator_id2"]
  }
}
Error:
403 Forbidden: User is not authorized to view the document.
json
Copy code
{
  "detail": "User not authorized to access this document"
}
5. Send a Document via Email
Path: /api/v1/secure/document/send
Method: POST
Description: Sends the document to all collaborators via email.
Headers:

http
Copy code
Authorization: Bearer <API_KEY>
Content-Type: application/json
Body Parameters:

json
Copy code
{
  "doc_id": "string"
}
Responses:

Success:
json
Copy code
{
  "message": "Document doc123 has been sent to all collaborators."
}
Error:
400 Bad Request: Document does not exist.
json
Copy code
{
  "detail": "Document does not exist"
}
Contoh Penggunaan dengan cURL
1. Create a New Document
bash
Copy code
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/create" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123"}'
2. Update a Document
bash
Copy code
curl -X PUT "https://tubestst-production.up.railway.app/api/v1/secure/document/update" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123", "content": "Updated content"}'
3. Add a Collaborator
bash
Copy code
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/add-collaborator" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123", "collaborator_id": "mUP7PpTHmFAkxcQLWKMY8t"}'
4. View a Document
bash
Copy code
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/view" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123"}'
5. Send a Document via Email
bash
Copy code
curl -X POST "https://tubestst-production.up.railway.app/api/v1/secure/document/send" \
     -H "Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "doc123"}'
