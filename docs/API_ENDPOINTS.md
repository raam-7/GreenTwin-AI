# GreenTwin AI API Contract

This document describes the API contract for the GreenTwin AI project. Unless stated otherwise, requests and responses use `application/json`.

## Shared conventions

- Protected endpoints require `Authorization: Bearer <access_token>`.
- IDs are UUID strings.
- Dates and times use ISO 8601 format in UTC, for example `2026-08-08T10:30:00Z`.
- Error responses use this shape:

```json
{
  "detail": "A clear explanation of the error"
}
```

## AUTH

### POST `/api/auth/login`

**Purpose:** Authenticate a registered user and return an access token.

**HTTP method:** `POST`

**URL:** `/api/auth/login`

**Authentication requirement:** None.

**Request body:**

```json
{
  "email": "student@greentwin.ai",
  "password": "correct-horse-battery-staple"
}
```

**Response body:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyLTEyMyJ9.signature",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "6c5d5c3d-84bc-4c8c-9d8d-7d15a5dd3b12",
    "name": "Asha Patel",
    "email": "student@greentwin.ai",
    "role": "field_officer"
  }
}
```

**Success status code:** `200 OK`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `422 Unprocessable Entity`

## NURSERIES

### POST `/api/nurseries`

**Purpose:** Create a nursery where saplings are raised and tracked.

**HTTP method:** `POST`

**URL:** `/api/nurseries`

**Authentication requirement:** Required.

**Request body:**

```json
{
  "name": "Green Valley Nursery",
  "location": "Pune, Maharashtra",
  "latitude": 18.5204,
  "longitude": 73.8567,
  "manager_name": "Ravi Kumar",
  "capacity": 5000
}
```

**Response body:**

```json
{
  "id": "f5a5dfcb-1f55-44d0-a40b-8e381b7dbb5a",
  "name": "Green Valley Nursery",
  "location": "Pune, Maharashtra",
  "latitude": 18.5204,
  "longitude": 73.8567,
  "manager_name": "Ravi Kumar",
  "capacity": 5000,
  "created_at": "2026-08-08T10:30:00Z"
}
```

**Success status code:** `201 Created`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `409 Conflict`, `422 Unprocessable Entity`

### GET `/api/nurseries`

**Purpose:** List nurseries available to the authenticated user.

**HTTP method:** `GET`

**URL:** `/api/nurseries`

**Authentication requirement:** Required.

**Request body:** None. Optional query parameters may include `page`, `page_size`, and `location`.

**Response body:**

```json
{
  "items": [
    {
      "id": "f5a5dfcb-1f55-44d0-a40b-8e381b7dbb5a",
      "name": "Green Valley Nursery",
      "location": "Pune, Maharashtra",
      "capacity": 5000,
      "sapling_count": 1240
    }
  ],
  "page": 1,
  "page_size": 20,
  "total": 1
}
```

**Success status code:** `200 OK`

**Common error status codes:** `401 Unauthorized`, `422 Unprocessable Entity`

## SAPLINGS

### POST `/api/saplings`

**Purpose:** Register a sapling in a nursery for lifecycle tracking and AI grading.

**HTTP method:** `POST`

**URL:** `/api/saplings`

**Authentication requirement:** Required.

**Request body:**

```json
{
  "nursery_id": "f5a5dfcb-1f55-44d0-a40b-8e381b7dbb5a",
  "species": "Neem",
  "source": "Local seed collection",
  "image_url": "https://storage.example.org/saplings/sapling-001.jpg"
}
```

**Response body:**

```json
{
  "id": "c1b4f0b5-12c7-4e52-bf03-5d57596b17e2",
  "nursery_id": "f5a5dfcb-1f55-44d0-a40b-8e381b7dbb5a",
  "species": "Neem",
  "source": "Local seed collection",
  "image_url": "https://storage.example.org/saplings/sapling-001.jpg",
  "grade": null,
  "created_at": "2026-08-08T10:35:00Z"
}
```

**Success status code:** `201 Created`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `409 Conflict`, `422 Unprocessable Entity`

### GET `/api/saplings/{id}`

**Purpose:** Retrieve the details and current grading information for one sapling.

**HTTP method:** `GET`

**URL:** `/api/saplings/{id}`

**Authentication requirement:** Required.

**Request body:** None. Replace `{id}` with the sapling UUID.

**Response body:**

```json
{
  "id": "c1b4f0b5-12c7-4e52-bf03-5d57596b17e2",
  "nursery_id": "f5a5dfcb-1f55-44d0-a40b-8e381b7dbb5a",
  "species": "Neem",
  "planting_date": "2026-07-15",
  "grade": "A",
  "grade_confidence": 0.94,
  "latest_health_status": "Healthy",
  "created_at": "2026-08-08T10:35:00Z"
}
```

**Success status code:** `200 OK`

**Common error status codes:** `401 Unauthorized`, `404 Not Found`, `422 Unprocessable Entity`

## PLANTATIONS

### POST `/api/plantations`

**Purpose:** Create a plantation site and record the planned planting activity.

**HTTP method:** `POST`

**URL:** `/api/plantations`

**Authentication requirement:** Required.

**Request body:**

```json
{
  "name": "Riverbank Restoration Site",
  "location": "Nashik, Maharashtra",
  "latitude": 20.0059,
  "longitude": 73.791,
  "area_hectares": 12.5,
  "planting_date": "2026-08-20",
  "sapling_ids": [
    "c1b4f0b5-12c7-4e52-bf03-5d57596b17e2"
  ]
}
```

**Response body:**

```json
{
  "id": "3f3d9e58-a6d3-43dd-9d5c-62f5f80a0a16",
  "name": "Riverbank Restoration Site",
  "location": "Nashik, Maharashtra",
  "latitude": 20.0059,
  "longitude": 73.791,
  "area_hectares": 12.5,
  "planting_date": "2026-08-20",
  "sapling_count": 1,
  "created_at": "2026-08-08T10:40:00Z"
}
```

**Success status code:** `201 Created`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `409 Conflict`, `422 Unprocessable Entity`

## MONITORING

### POST `/api/monitoring`

**Purpose:** Record an observation of a planted sapling or tree, including its location and image.

**HTTP method:** `POST`

**URL:** `/api/monitoring`

**Authentication requirement:** Required.

**Request body:**

```json
{
  "plantation_id": "3f3d9e58-a6d3-43dd-9d5c-62f5f80a0a16",
  "sapling_id": "c1b4f0b5-12c7-4e52-bf03-5d57596b17e2",
  "observed_at": "2026-08-08T11:00:00Z",
  "latitude": 20.0061,
  "longitude": 73.7908,
  "image_url": "https://storage.example.org/monitoring/tree-001.jpg",
  "notes": "New leaves observed after rainfall."
}
```

**Response body:**

```json
{
  "id": "ab2a2d0a-13f3-46ca-b3c2-dc3bc6f3ad10",
  "plantation_id": "3f3d9e58-a6d3-43dd-9d5c-62f5f80a0a16",
  "sapling_id": "c1b4f0b5-12c7-4e52-bf03-5d57596b17e2",
  "observed_at": "2026-08-08T11:00:00Z",
  "image_url": "https://storage.example.org/monitoring/tree-001.jpg",
  "created_at": "2026-08-08T11:01:00Z"
}
```

**Success status code:** `201 Created`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `422 Unprocessable Entity`

## AI

### POST `/api/ai/grade`

**Purpose:** Grade the quality of a nursery sapling from an image.

**HTTP method:** `POST`

**URL:** `/api/ai/grade`

**Authentication requirement:** Required.

**Request body:** Provide `sapling_id` and a sapling image as multipart form data.

Example request metadata:

```text
Content-Type: multipart/form-data
sapling_id: c1b4f0b5-12c7-4e52-bf03-5d57596b17e2
image: neem-sapling-001.jpg
```

**Response body:**

```json
{
  "sapling_id": "c1b4f0b5-12c7-4e52-bf03-5d57596b17e2",
  "grade": "A",
  "confidence": 0.94
}
```

Allowed `grade` values are `A`, `B`, and `C`. `confidence` is a number from `0` to `1`.

**Success status code:** `200 OK`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `413 Payload Too Large`, `415 Unsupported Media Type`, `422 Unprocessable Entity`

### POST `/api/ai/health`

**Purpose:** Assess tree health from a tree or monitoring image.

**HTTP method:** `POST`

**URL:** `/api/ai/health`

**Authentication requirement:** Required.

**Request body:** Provide `sapling_id`, `monitoring_id`, and a tree or monitoring image as multipart form data.

Example request metadata:

```text
Content-Type: multipart/form-data
sapling_id: c1b4f0b5-12c7-4e52-bf03-5d57596b17e2
monitoring_id: ab2a2d0a-13f3-46ca-b3c2-dc3bc6f3ad10
image: riverbank-tree-001.jpg
```

**Response body:**

```json
{
  "sapling_id": "c1b4f0b5-12c7-4e52-bf03-5d57596b17e2",
  "monitoring_id": "ab2a2d0a-13f3-46ca-b3c2-dc3bc6f3ad10",
  "status": "Healthy",
  "confidence": 0.91
}
```

Allowed `status` values are `Healthy`, `Stressed`, and `Dead`. `confidence` is a number from `0` to `1`.

**Success status code:** `200 OK`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `413 Payload Too Large`, `415 Unsupported Media Type`, `422 Unprocessable Entity`

## ANALYTICS

### GET `/api/analytics/dashboard`

**Purpose:** Return summary metrics for the authenticated user's nurseries and plantations.

**HTTP method:** `GET`

**URL:** `/api/analytics/dashboard`

**Authentication requirement:** Required.

**Request body:** None. Optional query parameters may include `nursery_id`, `plantation_id`, `from`, and `to`.

**Response body:**

```json
{
  "period": {
    "from": "2026-08-01",
    "to": "2026-08-08"
  },
  "nurseries": 3,
  "plantations": 8,
  "total_saplings": 1240,
  "grade_counts": {
    "A": 680,
    "B": 420,
    "C": 140
  },
  "health_counts": {
    "Healthy": 920,
    "Stressed": 250,
    "Dead": 70
  },
  "survival_rate": 0.943
}
```

**Success status code:** `200 OK`

**Common error status codes:** `401 Unauthorized`, `404 Not Found`, `422 Unprocessable Entity`

## RECOMMENDATIONS

### POST `/api/recommendations`

**Purpose:** Generate planting or care recommendations using site conditions and available GreenTwin AI data.

Future recommendations may include species recommendation, predicted survival probability, and care recommendations.

**HTTP method:** `POST`

**URL:** `/api/recommendations`

**Authentication requirement:** Required.

**Request body:**

```json
{
  "plantation_id": "3f3d9e58-a6d3-43dd-9d5c-62f5f80a0a16",
  "soil_type": "Sandy loam",
  "rainfall_mm": 82.5,
  "temperature_c": 28.4,
  "season": "Monsoon",
  "goal": "Improve sapling survival"
}
```

**Response body:**

```json
{
  "plantation_id": "3f3d9e58-a6d3-43dd-9d5c-62f5f80a0a16",
  "recommendations": [
    {
      "category": "watering",
      "title": "Reduce watering frequency",
      "description": "Recent rainfall is sufficient; check soil moisture before watering.",
      "priority": "medium"
    },
    {
      "category": "species",
      "title": "Use native drought-tolerant species",
      "description": "Consider Neem and Indian beech for the next planting batch.",
      "priority": "high"
    }
  ],
  "generated_at": "2026-08-08T11:10:00Z"
}
```

**Success status code:** `200 OK`

**Common error status codes:** `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `422 Unprocessable Entity`, `503 Service Unavailable`
