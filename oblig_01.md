# MANDATORY EXERCISE no. 1 


Delivery file: 1: (simpsons.ttl, simpsons.n3, simpsons.rdf or simpsons.nt). 

Read the whole of this document thoroughly before solving any of the exercises. 
The aim of these exercises is to capture family relations of the Simpsons family in RDF. To give you an overview of how parts the Simpson family looks like checking their family tree on the Simpson’s Wikia. 
When solving the exercises and modeling family relationships use only the classes 

- fam:Family  
- foaf:Person 
the properties 
- rdf:type
- foaf:age
- foaf:name
- fam:hasFamilyMember (relating a family to a member) 
- fam:hasBrother (relating a person to a brother)
- fam:hasSister (relating a person to a sister) 
- fam:hasParent (relating a person to a parent) 
- fam:hasMother (relating a person to a mother) 
- fam:hasFather (relating a person to a father) 
- fam:hasSpouse (relating a person to a spouse)

where foaf: is the prefix for the [FOAF vocabulary namespace](http://xmlns.com/foaf/0.1/) 
and fam: is the prefix for [this namespace](http://www.ifi.uio.no/INF3580/family#) 
1 
You may also use the standard xsd datatypes, and the prefix sim, which is shorthand for the namespace 
http://www.ifi.uio.no/INF3580/simpsons# 
Use the RDF serialization you prefer, RDF/XML, Turtle, N3, or N-Triples, but make sure your work is syntactically correct. We recommend that you use Turtle. RDF validators are available online: 
• http://www.w3.org/RDF/Validator/ (RDF/XML only) 
• http://www.easyrdf.org/converter (Turtle, RDF/XML, N3, etc. just convert to the same) 
• http://ttl.summerofcode.be/ (Turtle) 
Each Simpsons character mentioned in the exercise text shall be modeled as an instance of foaf:Person and is to be placed in the sim namespace. The localname identifier for each person should be their first name, e.g., the triple
sim:Homer rdf:type foaf:Person . 
is the intended way of stating that Homer Simpson is a person. Remember that RDF is case-sensitive. 
Solutions to all of the exercises below shall be put in the same RDF file. 
1 Exercise 
Define the standard rdf and xsd namespaces, and the foaf, fam, and sim namespaces as specified above in your RDF file. 
2 Exercise 
Add Homer, Marge, Lisa, Bart, and Maggie as instances of foaf:Person to your RDF file. Add also their full name, e.g. "Homer Simpson", using the foaf:name property and their age using the foaf:age property. Take values from the table below. Specify the age values to be of the datatype xsd:int. 
Person Age 
Homer Simpson 36
Marge Simpson 34
Lisa Simpson 8 
Bart Simpson 10 
Maggie Simpson 1 
3 Exercise 
Model the statement: "The Simpsons is a family, and members of the family are Marge, Homer, Bart, Lisa, and Maggie. Marge and Homer are married, i.e, Marge is the spouse of Homer and Homer is the spouse of Marge, and they are respectively the mother and father to Bart, Lisa and Maggie." Create a suitable identifier for the Simpsons family. 

4 Exercise 
Model the statement: "Maggie has the grandfather Abraham and the grandmother Mona." 
Tip: You do not know which of the grandparents is a parent to which of Maggie’s parents (since you only know what these exercises tell you). To express the relationship between Maggie and her grandparents, you’ll need to use blank nodes. 
5 Exercise 
Model the statement: "Lisa has the aunts Patty and Selma and the uncle Herb. Patty and Selma are sisters." 
6 Exercise 
Model the statement: "Marge has a father-in-law Abraham." 
7 Ending notes 
7.1 Delivery
Your delivery shall include one file called simpsons.xxx, where .xxx is an extension indicating the RDF serialisation used in the file: .rdf = RDF/XML, .ttl = Turtle, .n3 = N3 and .nt = N-Triples. 
7.2 Testing 
You can, and should, use Mr. Oblig to test your delivery before handing it in. Mr. Oblig is located at http://sws.ifi.uio.no/mroblig/. Note that Mr. Oblig comes without any warranty. A non-functioning Mr. Oblig will not have any effect on the due date of this mandatory exercise, and a flawless test report from Mr. Oblig does not guarantee that your delivery will be graded with passed. Also, since there may be many correct answers to an exercise, it is possible that Mr. Oblig does not agree with your solution even though it is correct. However, a perfect score from Mr. Oblig is an indication that your delivery is good and that it does not contain any "stupid" errors. 
Good Luck! 

