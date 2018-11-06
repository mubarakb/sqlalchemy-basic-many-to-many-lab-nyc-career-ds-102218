from models import *

def return_christian_bales_roles(session):
    bale= session.query(Actor).filter_by(name= 'Christian Bale').first()
    return bale.roles
    # Return a list of Christian Bale role instances

def return_catwoman_actors(session):
    return session.query(Role).filter_by(character= 'Catwoman').first().actors
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors(session):
    return len(session.query(Role).filter_by(character= 'Batman').first().actors)
    # Return the number of actors that have played Batman
