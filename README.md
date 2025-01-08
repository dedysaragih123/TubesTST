# TubesTST API Documentation

This documentation provides instructions for using the API endpoints available in the TubesTST project. The API allows authenticated users to create, update, manage, and collaborate on documents.

---

## **Base URL**

https://tubestst-production.up.railway.app/

---

## **Authentication**

The API uses **API Key Authentication**. Include a valid API key in the `Authorization` header for all protected routes:

Authorization: Bearer <API_KEY>


### **Predefined API Keys**
| **API Key**                              | **User Name** | **Email**             |
|------------------------------------------|---------------|-----------------------|
| `e54d4431-5dab-474e-b71a-0db1fcb9e659`  | Arvyno        | arvyno@example.com    |
| `5f0c7127-3be9-4488-b801-c7b6415b45e9`  | Bastian       | bastian@example.com   |

---

## **Endpoints**

### **1. Create a New Document**
---

**Method**:  
`POST`

**URL**:  
`/api/v1/secure/document/create`

**Description**:  
Creates a new document owned by the authenticated user.

#### **Headers**
- Authorization: Bearer `<API_KEY>`
- Content-Type: application/json

#### **Body Parameters**
| Parameter | Type   | Description                       |
|-----------|--------|-----------------------------------|
| `doc_id`  | String | A unique identifier for the document. |

#### **Example Request**

POST /api/v1/secure/document/create HTTP/1.1 Host: tubestst-production.up.railway.app Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659 Content-Type: application/json

{ "doc_id": "doc123" }

markdown
Copy code

#### **Response**
- **Success**:
{ "message": "Document doc123 created successfully." }

- **Error (400)**:
{ "detail": "Document ID already exists" }


---

### **2. Update an Existing Document**
---

**Method**:  
`PUT`

**URL**:  
`/api/v1/secure/document/update`

**Description**:  
Updates the content of an existing document.

#### **Headers**
- Authorization: Bearer `<API_KEY>`
- Content-Type: application/json

#### **Body Parameters**
| Parameter   | Type   | Description                    |
|-------------|--------|--------------------------------|
| `doc_id`    | String | The unique identifier of the document. |
| `content`   | String | The updated content of the document. |

#### **Example Request**

PUT /api/v1/secure/document/update HTTP/1.1 Host: tubestst-production.up.railway.app Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659 Content-Type: application/json

{ "doc_id": "doc123", "content": "Updated document content." }


#### **Response**
- **Success**:
{ "message": "Document doc123 updated successfully." }

- **Error (400)**:
{ "detail": "User not authorized to edit this document" }


---

### **3. Add a Collaborator to a Document**
---

**Method**:  
`POST`

**URL**:  
`/api/v1/secure/document/add-collaborator`

**Description**:  
Adds a collaborator to an existing document.

#### **Headers**
- Authorization: Bearer `<API_KEY>`
- Content-Type: application/json

#### **Body Parameters**
| Parameter         | Type   | Description                             |
|-------------------|--------|-----------------------------------------|
| `doc_id`          | String | The unique identifier of the document. |
| `collaborator_id` | String | The user ID of the collaborator.        |

#### **Example Request**

POST /api/v1/secure/document/add-collaborator HTTP/1.1 Host: tubestst-production.up.railway.app Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659 Content-Type: application/json

{ "doc_id": "doc123", "collaborator_id": "mUP7PpTHmFAkxcQLWKMY8t" }


#### **Response**
- **Success**:
{ "message": "User Bastian added as a collaborator to document doc123." }

#### **Response**
- **Success**:
{ "detail": "Document does not exist" }

- **Error (400)**:
{ "message": "User Bastian is already a collaborator for document doc123." }


---

### **4. View a Document**
---

**Method**:  
`POST`

**URL**:  
`/api/v1/secure/document/view`

**Description**:  
Retrieves the content of a document.

#### **Headers**
- Authorization: Bearer `<API_KEY>`
- Content-Type: application/json

#### **Body Parameters**
| Parameter | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| `doc_id`  | String | The unique identifier of the document.  |

#### **Example Request**

POST /api/v1/secure/document/view HTTP/1.1 Host: tubestst-production.up.railway.app Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659 Content-Type: application/json

{ "doc_id": "doc123" }

#### **Response**
- **Success**:
{ "document": { "content": "Document content here.", "collaborators": ["collaborator_id1", "collaborator_id2"] } }

- **Error (403)**:
{ "detail": "User not authorized to access this document" }


---

### **5. Send a Document via Email**
---

**Method**:  
`POST`

**URL**:  
`/api/v1/secure/document/send`

**Description**:  
Sends a document to all collaborators via email.

#### **Headers**
- Authorization: Bearer `<API_KEY>`
- Content-Type: application/json

#### **Body Parameters**
| Parameter | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| `doc_id`  | String | The unique identifier of the document.  |

#### **Example Request**
POST /api/v1/secure/document/send HTTP/1.1 Host: tubestst-production.up.railway.app Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659 Content-Type: application/json

{ "doc_id": "doc123" }


#### **Response**
- **Success**:
{ "message": "Document doc123 has been sent to all collaborators." }

- **Error (400)**:
{ "detail": "Document does not exist" }


---

## **Examples**

### **Using Postman**

#### **1. Create a New Document**
- **Method**: `POST`  
- **URL**:  
https://tubestst-production.up.railway.app/api/v1/secure/document/create

- **Headers**:  
   `Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659`  
   `Content-Type: application/json`  
- **Body**:  
{
  "doc_id": "doc123"
}

---

#### **2. Update a New Document**
- **Method**: `PUT`  
- **URL**:  
https://tubestst-production.up.railway.app/api/v1/secure/document/update

- **Headers**:  
   `Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659`  
   `Content-Type: application/json`  
- **Body**:
 {
  "doc_id": "doc123",
  "content": "Updated document content."
 }

---

#### **3. Add a Collaborator**
- **Method**: `POST`  
- **URL**:  
https://tubestst-production.up.railway.app/api/v1/secure/document/add-collaborator

- **Headers**:  
   `Authorization: Bearer e54d4431-5dab-474e-b71a-0db1fcb9e659`  
   `Content-Type: application/json`  
- **Body**:
 {
  "doc_id": "doc123",
  "collaborator_id": "mUP7PpTHmFAkxcQLWKMY8t"
 }
