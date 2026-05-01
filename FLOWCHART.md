# Crypto App - Flowchart

## Application Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    START APPLICATION                        │
│                  (python app.py)                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    HOME PAGE                                │
│              (http://localhost:5000)                        │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  Encryption  │  │  Decryption  │  │   Hashing    │   │
│  │     Button   │  │    Button    │  │    Button    │   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │
└─────────┼──────────────────┼──────────────────┼────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
    ┌─────────┐        ┌─────────┐        ┌─────────┐
    │Encryption│        │Decryption│       │ Hashing │
    │  Page    │        │  Page    │       │  Page   │
    └────┬─────┘        └────┬─────┘       └────┬────┘
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────────────────────────────────────────────────┐
│              SELECT CRYPTOGRAPHIC METHOD                    │
│                                                             │
│  Encryption Methods:        Decryption Methods:            │
│  • Monoalphabetic          • Monoalphabetic                │
│  • Hill Cipher             • RC4                           │
│  • Columnar Transposition  • CBC                           │
│  • RC4                     • OFB                           │
│  • CBC                     • CTR                           │
│  • OFB                                                      │
│  • CTR                                                      │
│                                                             │
│  Hashing Methods:                                          │
│  • MAC                                                     │
│  • SHA-1                                                   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    MODAL POPUP                              │
│              (Input/Output Window)                          │
│                                                             │
│  ┌─────────────────────────────────────────────┐          │
│  │  Method Name - Operation Type              │          │
│  │                                             │          │
│  │  Label: "Enter text to..."                 │          │
│  │  ┌─────────────────────────────────────┐   │          │
│  │  │  Text Area (User Input)              │   │          │
│  │  └─────────────────────────────────────┘   │          │
│  │                                             │          │
│  │  [Start Encryption/Decryption/Hashing]     │          │
│  │                                             │          │
│  │  Result Area:                               │          │
│  │  ┌─────────────────────────────────────┐   │          │
│  │  │  Output Text Area (Read-only)         │   │          │
│  │  └─────────────────────────────────────┘   │          │
│  │                                             │          │
│  │  Status Message                             │          │
│  └─────────────────────────────────────────────┘          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              USER CLICKS "START" BUTTON                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              VALIDATE INPUT                                 │
│                                                             │
│  IF input is empty:                                         │
│    └─► Show error: "Please enter text first."              │
│    └─► Return to input                                      │
│                                                             │
│  IF input is valid:                                         │
│    └─► Continue to processing                               │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              SET LOADING STATE                              │
│                                                             │
│  • Disable "Start" button                                   │
│  • Show "Processing..." message                             │
│  • Display loading indicator                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              BUILD API ENDPOINT                              │
│                                                             │
│  Format: /api/{operation}/{method-name}                    │
│                                                             │
│  Examples:                                                  │
│  • /api/encryption/rc4                                      │
│  • /api/decryption/cbc                                      │
│  • /api/hashing/sha-1                                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              SEND HTTP POST REQUEST                         │
│                                                             │
│  Method: POST                                               │
│  Headers: Content-Type: application/json                   │
│  Body: { "text": "user input text" }                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              FLASK SERVER (app.py)                          │
│                                                             │
│  Route Handler:                                             │
│  • /api/encryption/<method>                                 │
│  • /api/decryption/<method>                                 │
│  • /api/hashing/<method>                                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              PROCESS REQUEST                                │
│                                                             │
│  1. Normalize method name                                   │
│  2. Find method in dictionary                               │
│  3. Extract text from JSON body                             │
│  4. Validate input                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              CALL CRYPTO MODULE                              │
│                                                             │
│  crypto_modules/                                            │
│  ├── {method}_encryption.py                                │
│  ├── {method}_decryption.py                                │
│  └── {method}_hashing.py                                   │
│                                                             │
│  Function: process_text(text)                               │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              EXECUTE CRYPTOGRAPHIC OPERATION                │
│                                                             │
│  Encryption:                                                │
│    Plaintext → Algorithm → Ciphertext                      │
│                                                             │
│  Decryption:                                                │
│    Ciphertext → Algorithm → Plaintext                       │
│                                                             │
│  Hashing:                                                   │
│    Text → Hash Function → Hash Value                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              RETURN RESULT                                  │
│                                                             │
│  JSON Response:                                             │
│  {                                                          │
│    "method": "RC4",                                         │
│    "input_text": "...",                                     │
│    "output": "encrypted/decrypted/hashed result"            │
│  }                                                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              HANDLE RESPONSE (JavaScript)                   │
│                                                             │
│  IF response.ok:                                            │
│    └─► Display output in text area                          │
│    └─► Show success message                                │
│    └─► Enable "Start" button                                │
│                                                             │
│  IF response.error:                                         │
│    └─► Display error message                               │
│    └─► Clear output area                                   │
│    └─► Enable "Start" button                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              DISPLAY RESULTS                                │
│                                                             │
│  • Output text in read-only textarea                        │
│  • Status message (success/error)                           │
│  • User can copy result                                     │
│  • User can close modal or process another text             │
└─────────────────────────────────────────────────────────────┘
```

## Detailed Component Flow

### Encryption Flow
```
User Input → Select Method → Enter Text → API Call → 
Crypto Module → Encrypt → Return Ciphertext → Display
```

### Decryption Flow
```
User Input → Select Method → Enter Ciphertext → API Call → 
Crypto Module → Decrypt → Return Plaintext → Display
```

### Hashing Flow
```
User Input → Select Method → Enter Text → API Call → 
Crypto Module → Hash → Return Hash Value → Display
```

## Error Handling Flow

```
┌─────────────────┐
│  Error Occurs   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  Check Error Type                   │
│                                     │
│  • Network Error                    │
│  • Server Error (500)               │
│  • Client Error (400, 404)          │
│  • Validation Error                 │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  Display Error Message              │
│  • Show in status message area      │
│  • Use error styling (red)         │
│  • Keep input for user to retry     │
└─────────────────────────────────────┘
```

## Navigation Flow

```
Home Page
    │
    ├─► Encryption Page
    │       │
    │       └─► Back to Home
    │
    ├─► Decryption Page
    │       │
    │       └─► Back to Home
    │
    └─► Hashing Page
            │
            └─► Back to Home
```

## Data Flow Diagram

```
┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
│  Client  │─────►│  Flask   │─────►│  Crypto  │─────►│  Result  │
│ (Browser)│      │  Server  │      │  Module  │      │          │
└──────────┘      └──────────┘      └──────────┘      └──────────┘
     ▲                                                      │
     │                                                      │
     └──────────────────────────────────────────────────────┘
                    (JSON Response)
```

---

**Legend:**
- `┌─┐` = Process/Component
- `─►` = Data/Control Flow
- `│` = Sequential Flow
- `├─` = Branch/Decision

