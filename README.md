# Project: Organizing and Running Games from the `/data` Directory

## Assumptions
- The `/data` directory contains various files and subdirectories.
- You are only interested in directories related to games.
- Each **game** directory's name contains the word **"game"**.
- Each **game** directory has a single `.go` file that needs to be compiled and run.

---

## Steps and Requirements

### 1. Find All Game Directories from `/data`
- Locate all directories within `/data` that contain the word **"game"**.

### 2. Create a New `/games` Directory
- Create a new directory called `/games` to store the renamed game directories.

### 3. Copy and Rename Game Directories
- Copy each **game** directory to `/games`, removing the **"game"** suffix from their names.  
  - **Example:**
    - `/data/spacegame` → `/games/space`.

### 4. Create a JSON File with Game Information
- Generate a `.json` file listing the names and paths of the games in the `/games` directory.

### 5. Compile All Game Code
- Compile each `.go` file found in the `/games` directory using the Go compiler (`go build`).

### 6. Run All Game Code
- Execute the compiled binaries of the games.

---

## Sample JSON Structure
```json
{
  "games": [
    {
      "name": "space",
      "path": "/games/space"
    },
    {
      "name": "adventure",
      "path": "/games/adventure"
    }
  ]
}

