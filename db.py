from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.testmaker

def get_all_quizes_of_section(section_name):
    """Get all quizzes belonging to this section"""
    coll = db.quizes
    quizes = coll.find({"section": section_name})
    return list(quizes)

def get_all_questions_of_quiz(quiz_id):
    """Gets all the questions of this quiz id"""
    coll = db.questions
    questions = coll.find({"quiz_id": quiz_id})
    return list(questions)

def create_new_section(section_name):
    """Makes a new section"""
    coll = db.sections
    if coll.find_one({'section_name': section_name}):
        return False, 400
    else:
        coll.insert_one({'section_name': section_name})
        return True, 200

def get_sections_and_quiz_data():
    """Returns a list of sections and their internal data"""
    sections_coll = db.sections
    quizes_coll = db.quizes
    
    # Get all section names
    sections = sections_coll.find()
    
    result = []
    
    for section in sections:
        section_name = section.get('section_name')
        
        # Fetch quiz data for the section
        quizes = quizes_coll.find({'section': section_name})
        
        quiz_names = []
        total_duration = 0

        for quiz in quizes:
            quiz_names.append(quiz.get('quiz_name'))
            total_duration += quiz.get('duration', 0)
        
        result.append({
            'section_name': section_name,
            'quiz_names': quiz_names,
            'total_duration': total_duration
        })
    
    return result
