# SKIntellet 🧴🧠

**SKIntellet** is an AI-powered skin analysis platform designed to help users better understand their skin health. By leveraging computer vision techniques, the platform detects common skin conditions like acne and oiliness, offers personalized skincare product recommendations, and even allows users to book dermatologist consultations — all from a single interface.

---

## 🌟 Features

- 🔍 **Skin Condition Detection**  
  Uses advanced image processing and machine learning (YOLO) to detect acne, oiliness, and other visible skin concerns from facial images.

- 🧴 **Personalized Skincare Recommendations**  
  Suggests suitable skincare products based on the user's detected skin condition and type.

- 🩺 **Dermatologist Booking**  
  Enables users to schedule consultations with certified dermatologists through the platform.

---

## 🧠 Tech Stack

- **Frontend**: HTML / CSS  
- **Backend**: Flask  
- **AI Model**: YOLO (You Only Look Once) for skin condition detection  
- **Libraries**: OpenCV, TensorFlow / PyTorch , NumPy, Pandas
- 
---

## 🛠️ How It Works

1. **Image Upload**: User uploads a clear facial image.
2. **AI Processing**: The image is processed by a YOLO-based model to detect acne and oiliness.
3. **Analysis Report**: The app generates a skin health report.
4. **Product Recommendations**: Based on the report, relevant skincare products are suggested.
5. **Booking Option**: Users can book dermatologist appointments if further care is needed.

---

## 📸 Sample Output

> Add screenshots or demo GIFs here showing the analysis results and recommendations.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip
- Virtual environment (recommended)

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/SKinTellet.git
cd SKinTellet

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the backend
python app.py


