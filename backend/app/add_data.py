from sqlalchemy.orm import Session
from .models import SessionLocal, PersonData

# Function to add data to the database
def add_person_data(db_session: Session, num_bboxes: int, result_image_file_path: str):
    db_entry = PersonData(num_bboxes=num_bboxes, result_image_file_path=result_image_file_path)
    db_session.add(db_entry)
    db_session.commit()
    db_session.refresh(db_entry)
    return db_entry

# Example usage: Add a new record to the database
if __name__ == "__main__":
    db_session = SessionLocal()

    # Example data to add
    num_bboxes = 5  # Example: number of bounding boxes detected in the image
    result_image_file_path = "path/to/result_image.jpg"  # Example: file path of the result image

    # Add the data to the database
    new_record = add_person_data(db_session, num_bboxes, result_image_file_path)
    print(f"Data added: Time: {new_record.time}, Bboxes: {new_record.num_bboxes}, Image Path: {new_record.result_image_file_path}")
