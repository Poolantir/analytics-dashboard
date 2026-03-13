## Poolantir Analytics Dashboard

### Tech stack
- **Plotly Dash**
- **Dash Mantine Components**
- **Docker**
- **Firebase Firestore**

### Running with Docker

Build the image (run from the project root):

```bash
docker build -t poolantir-dashboard -f app/Dockerfile .
```

Run the container (forward port 8050 by default):

```bash
docker run poolantir-dashboard poolantir-dashboard
```

Then open `http://localhost:8050` in your browser.
