import kaidame
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///{0}'.format(kaidame.dbasefile), echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
Session.configure(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                         self.name, self.fullname, self.password)

class AnimeTitles(Base):
    __tablename__ = 'animetitles'

    id = Column(Integer, primary_key=True)
    main = Column(String)
    mainshort = Column(String)
    title = Column(String)
    titleshort = Column(String)
    officialen = Column(String)
    officialjp = Column(String)
    imdbid = Column(String)
    tvrageid = Column(String)
    anidbid = Column(String)
    malid = Column(String)
    wikilink = Column(String)

    def __repr__(self):
        return"<AnimeTitles(main='%s',mainshort='%s', title='%s',titleshort='%s', officialen='%s', officialjp='%s'," \
              " imdbid='%s', tvrageid='%s', anidbid='%s', malid='%s', wikilink='%s')>" % (
            self.main, self.mainshort, self.title, self.titleshort, self.officialen, self.officialjp, self.imdbid,
            self.tvrageid, self.anidbid, self.malid, self.wikilink)


Base.metadata.create_all(engine)

#ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
#session.add(ed_user)
#session.commit

# for name, fullname in session.query(User.name, User.fullname):
#   print name, fullname
# ed Ed Jones
# wendy Wendy Williams
# mary Mary Contrary
# fred Fred Flinstone