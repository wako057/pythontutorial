#!/usr/bin/python

class Parent:        # define parent class
    parentAttr = 100
    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print 'Calling parent method'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute :", Parent.parentAttr


class Child(Parent): # define child class
    def __init__(self):
        print "Calling child constructor"


    def parentMethod(self):
        print "======== blutasse"
        Parent.parentMethod(self);
        print "On est dans parentMethod overrided"
        print "======== blutasse 2"

    def childMethod(self):
        print "===== Test calling parent before child"
        Parent.parentMethod(self);
        print 'Calling child method'
        print '===== Fin de test'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.getAttr()          # again call parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method