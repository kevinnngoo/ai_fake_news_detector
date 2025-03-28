from datetime import datetime
from bson import ObjectId
from flask import current_app

class Analysis:
    def __init__(self, text, result, confidence_score, user_id=None, _id=None):
        self._id = _id or ObjectId()
        self.text = text
        self.result = result
        self.confidence_score = confidence_score
        self.user_id = ObjectId(user_id) if user_id else None
        self.created_at = datetime.utcnow()

    @staticmethod
    def from_dict(data):
        return Analysis(
            text=data['text'],
            result=data['result'],
            confidence_score=data['confidence_score'],
            user_id=data.get('user_id'),
            _id=data.get('_id')
        )

    def to_dict(self):
        return {
            "_id": str(self._id),
            "text": self.text,
            "result": self.result,
            "confidence_score": self.confidence_score,
            "user_id": str(self.user_id) if self.user_id else None,
            "created_at": self.created_at
        }

    def save(self):
        analysis_dict = {
            "text": self.text,
            "result": self.result,
            "confidence_score": self.confidence_score,
            "user_id": self.user_id,
            "created_at": self.created_at
        }
        result = current_app.db.analyses.insert_one(analysis_dict)
        self._id = result.inserted_id
        return self

    @staticmethod
    def find_by_user(user_id):
        analyses = current_app.db.analyses.find({"user_id": ObjectId(user_id)})
        return [Analysis.from_dict(analysis) for analysis in analyses]
