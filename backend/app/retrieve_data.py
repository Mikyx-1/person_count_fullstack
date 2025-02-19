from sqlalchemy.orm import Session
from models import SessionLocal, PersonData

# Function to retrieve all data from the database
def get_all_person_data(db_session: Session):
    return db_session.query(PersonData).all()

# Example usage: Retrieve all data from the database
if __name__ == "__main__":
    db_session = SessionLocal()

    # Retrieve all records from the database
    people_data = get_all_person_data(db_session)

    # Print the retrieved data
    for record in people_data:
        print(f"Time: {record.time}, Bboxes: {record.num_bboxes}, Image Path: {record.result_image_file_path}")
