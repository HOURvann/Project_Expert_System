from app import create_app
from app.extensions import db
from app.models.rice_model import Symptom, Disease, Rule, User 

app = create_app()

# កូដនេះនឹងដំណើរការភ្លាមៗពេល Run
with app.app_context():
    print("1. កំពុងលុបទិន្នន័យចាស់ (Drop All)...")
    db.drop_all()
    
    print("2. កំពុងបង្កើតតារាងថ្មី (Create All)...")
    db.create_all()

    # --- បញ្ចូលទិន្នន័យ ---
    print("3. កំពុងបញ្ចូលទិន្នន័យ...")
    
    # Symptoms
    sym1 = Symptom(text="ស្លឹកមានស្នាមអុចៗ រាងដូចគ្រាប់ពេជ្រ (Blast)")
    sym2 = Symptom(text="ស្លឹកប្រែជាពណ៌លឿងក្រៀមពីចុងស្លឹក (Bacterial Blight)")
    sym3 = Symptom(text="ដើមស្រូវស្វិត ឬបាក់ត្រង់ក (Dead Heart)")
    sym4 = Symptom(text="កួរស្រូវមានពណ៌ស ស្វិត មិនដាក់គ្រាប់ (Whitehead)")
    sym5 = Symptom(text="មានស្នាមអុចពណ៌ត្នោត រាងមូលៗតូចៗ (Brown Spot)")
    db.session.add_all([sym1, sym2, sym3, sym4, sym5])

    # Diseases
    d1 = Disease(name="ជំងឺប្រេះស្លឹក (Rice Blast)", description="...", solution="...")
    d2 = Disease(name="ជំងឺបាក់តេរីស្លឹក (Bacterial Leaf Blight)", description="...", solution="...")
    d3 = Disease(name="ដង្កូវស៊ីដើម (Stem Borer)", description="...", solution="...")
    d4 = Disease(name="ជំងឺអុចត្នោត (Brown Spot)", description="...", solution="...")
    db.session.add_all([d1, d2, d3, d4])

    # Rules
    rules = [
        Rule(symptom_id=1, disease_id=1), # Blast -> Blast
        Rule(symptom_id=2, disease_id=2), # Leaf Yellow -> Bacterial
        Rule(symptom_id=3, disease_id=3), # Dead Heart -> Stem Borer
        Rule(symptom_id=4, disease_id=3), # Whitehead -> Stem Borer
        Rule(symptom_id=5, disease_id=4), # Brown Spot -> Brown Spot
    ]
    db.session.add_all(rules)

    # Users (សំខាន់សម្រាប់ Login)
    admin = User(username="admin", password="123", role="admin")
    staff = User(username="staff", password="123", role="staff")
    db.session.add_all([admin, staff])

    db.session.commit()
    print("✅ ជោគជ័យ! បញ្ចូលទិន្នន័យជំងឺ និង Users រួចរាល់!")