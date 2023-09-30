from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)


class TranslatedWord(Base):
    __tablename__ = 'translated_words'

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer, ForeignKey('words.id'))
    translated_word = Column(String, nullable=False)
