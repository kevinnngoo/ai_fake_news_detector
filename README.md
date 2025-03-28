# AI Fake News Detector

A web application that uses AI to detect and analyze potential fake news articles. Built with Flask, MongoDB, and React.

## 🚀 Features

- User authentication system
- Text analysis for fake news detection
- RESTful API architecture
- MongoDB database integration
- JWT-based security

## 🛠️ Tech Stack

### Backend

- Python 3.x
- Flask
- MongoDB
- JWT Authentication
- Python-dotenv

### Frontend (In Development)

- React.js
- React Router
- Axios
- Material UI (planned)

## 📋 Prerequisites

- Python 3.x
- MongoDB
- Node.js and npm (for frontend)
- Git

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/ai_fake_news_detector.git
cd ai_fake_news_detector
```

2. **Set up Backend**

```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # Windows
# OR
source venv/bin/activate     # Linux/Mac

pip install -r requirements.txt
```

3. **Configure Environment Variables**
   Create a `.env` file in the backend directory:

```env
JWT_SECRET_KEY=your_secret_key
MONGODB_URI=mongodb://localhost:27017/fake_news_detector
```

4. **Set up Frontend (Coming Soon)**

```bash
cd frontend
npm install
```

## 🚀 Running the Application

1. **Start Backend Server**

```bash
cd backend
flask run
```

The server will start at `http://localhost:5000`

2. **Start Frontend Development Server (Coming Soon)**

```bash
cd frontend
npm start
```

The frontend will be available at `http://localhost:3000`

## 📝 API Endpoints

### Authentication

- `POST /api/auth/login` - User login
  - Body: `{ "email": "user@example.com", "password": "password123" }`

### Analysis

- `POST /api/analyze` - Analyze text for fake news
  - Requires: JWT Authentication
  - Body: `{ "text": "Article text to analyze" }`

## 🔒 Security

- JWT-based authentication
- Password hashing
- Protected API endpoints
- Environment variable configuration

## 🛣️ Roadmap

- [ ] Implement user registration
- [ ] Add AI analysis model
- [ ] Create frontend UI
- [ ] Add result history
- [ ] Implement user dashboard
- [ ] Add social sharing features

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Kevin Ngo - kevinngo2002@gmail.com

Project Link: [https://github.com/yourusername/ai_fake_news_detector](https://github.com/kevinnngoo/ai_fake_news_detector)
