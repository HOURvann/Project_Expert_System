from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.rice_model import Symptom, Disease, Rule, User

rice_bp = Blueprint('rice', __name__)

# =========================================
# ១. ផ្នែកសម្រាប់កសិករ (Public / User)
# =========================================

@rice_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # ១. ទទួលយក ID នៃរោគសញ្ញាដែលកសិករបាន Tick
        selected_ids = request.form.getlist('symptoms')
        
        # ២. ស្វែងរកជំងឺដែលត្រូវនឹងរោគសញ្ញានោះ
        found_diseases = {} 
        
        if selected_ids:
            # រក Rule ណាដែលមាន Symptom ដូចគេ Tick
            rules = Rule.query.filter(Rule.symptom_id.in_(selected_ids)).all()
            
            for rule in rules:
                # យកជំងឺចេញពី Rule
                if rule.disease:
                    found_diseases[rule.disease.id] = rule.disease
        
        # ៣. បង្ហាញលទ្ធផល
        return render_template('rice/result.html', diseases=found_diseases.values())

    # ផ្នែក GET: បង្ហាញទម្រង់ឱ្យ Tick
    symptoms = Symptom.query.all()
    return render_template('rice/index.html', symptoms=symptoms)


# =========================================
# ២. ផ្នែកសម្រាប់ Admin (Login System)
# =========================================

@rice_bp.route('/login', methods=['GET', 'POST'])
def login():
    # បើ Login រួចហើយ ឱ្យទៅ Dashboard តែម្ដង
    if current_user.is_authenticated:
        return redirect(url_for('rice.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # ស្វែងរក User ក្នុង Database
        user = User.query.filter_by(username=username).first()
        
        # ផ្ទៀងផ្ទាត់លេខសម្ងាត់
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('rice.dashboard'))
        else:
            flash('ឈ្មោះ ឬលេខសម្ងាត់មិនត្រឹមត្រូវ!', 'danger')
            
    return render_template('rice/login.html')

@rice_bp.route('/dashboard')
@login_required  # <--- ការពារសុវត្ថិភាព (ទាល់តែ Login ទើបចូលបាន)
def dashboard():
    # ទាញយក User និង ជំងឺទាំងអស់មកបង្ហាញ
    all_users = User.query.all()
    all_diseases = Disease.query.all()
    return render_template('rice/dashboard.html', users=all_users, diseases=all_diseases)

@rice_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('rice.index'))