IN3060/IN4060 – MANDATORY EXERCISE 5 

Tiago Lubiana Alves
N USP 8945857
São Paulo, 11/11/2020

Delivery files: 3 files: 2 OWL files, 1 pdf file containing answers to questions. 

# 1.1 Manchester Syntax 
Express the statements 3, 4, 5, 13, 14, 15, 19, 21; and the three statements about individuals in Manchester syntax, e.g., no. 6: "Every warmblooded horse is a horse" can be written as (WarmbloodedHorse ⊑ Horse): 

Class: WarmbloodedHorse
    SubClassOf: Horse

3. Every horse is an animal. 

Class: Horse
        SubClassOf: Animal

4. Every animal is a male or a female. 

Class Animal:
        EquivalentTo: Male or Female

5. Nothing is both a male and a female. 
 
 DisjointClasses: Male, Female

13. Every monté horse is a racehorse that has only competed in monté races. 

Class: MonteHorse
        EquivalentTo: RaceHorse and (hasCompeted only MonteRace) 

14. A superhorse is by definition a racehorse that has won more than 100 horse races. 

Class: SuperHorse
        EquivalentTo: RaceHorse and (hasWon min 100 HorseRace) 

15. You must compete in a race to win a race. 

ObjectProperty: hasWon
        SubPropertyOf: hasCompeted

19.  Every racehorse has at least one trainer which is a person. 

Class: RaceHorse:
SubClassOf: 
        Horse  and (hasTrainer some Person)

21.  If a horse has a trainer, then this trainer trains the horse. 

ObjectProperty:hasTrainer

    InverseOf: 
        trains


1.2 Questions 
Answer the following questions with "Yes", "No" or "Unknown", and a sentence or two to back up the claim, referring to the axioms you have created in your ontology as arguments. 
1. Is Rex Rodney a male or a female animal? 

Yes. A SuperHorse is a Horse, which is an Animal, which is Male or Female. 

2. Does Kjell Håkonsen have an interest in Elitloppet 1986? 

Yes. he trains a horse that competed on that race. 

3. Is Rex Rodney a warmblooded horse?
Unknown. No assertions or inferences that allow such conclusion. 

4. Is Steady, Ready, Go a warmblooded horse?
No. Every warm-blooded horse which has competed in a monté race must be between 4–12 years old. Every monté horse is a racehorse that has only competed in monté races. The horse called "Steady, Ready, Go" is a filly and monté horse.

5. Is Steady, Ready, Go a coldblooded horse?
Unknown. The ColdBloodedHorse class is disjoint with WarmBloodedHorse, but we do not know if every horse is either ColdBloodedHorse or WarmBloodedHorse.

6. Did Steady, Ready, Go compete in Elitloppet 1986? 
No. Every monté horse is a racehorse that has only competed in monté races. Elitloppet1986 is not a monté race.

2 Exercise: Mapping DBpedia to your ontology 
The task of this exercise is to create a mapping of parts of the DBpedia vocabulary about horses and racehorses to your ontology from the exercise above. 
Below is an excerpt from the result of running a DESCRIBE query on the dbpedia.org SPARQL endpoint: http://dbpedia.org/sparql. The excerpt contains data about two racehorses, one of them is listed below, a racehorse called "In the Wings". The exercise is to create a mapping ontology that maps all properties mentioned in the excerpt to the ontology you created in the exercise above. 
The mapping shall be created by giving a series of axioms (i.e., sub- class/property and equivalence axioms) which relate the dbpedia properties to your classes and properties, e.g, 
dbpprop:dam owl:equivalentProperty :dam 
creates a mapping between the dbpprop:dam and "your" :dam property.
Note that the left-hand-side and right-hand-side of axioms can be complex classes or properties, e.g., dbpprop:horsename should be mapped to some combination of :name and :Horse (not only to :name) (Tip: you need to use the general class axioms feature in Protégé to express this.) 
Note the owl:equivalentProperty relation only applies to lists of properties:
axiom ::= 'EquivalentProperties(' URIreference URIreference  { URIreference } ')' ...

        The excerpt:
1 <http://dbpedia.org/resource/In_the_Wings_%28horse%29> 
2   dbpprop:f <http://dbpedia.org/resource/Sadler%27s_Wells_%28horse%29> ; 
3   dbpprop:ff [ dbpprop:name "Northern Dancer" ] ; 
4   dbpprop:fm [ dbpprop:name "Fairy Bridge" ] ; 
5   dbpprop:horsename "In the Wings" ; 
6   dbpprop:m [ dbpprop:name "High Hawk" ]; 
7   dbpprop:mf dbpedia:Shirley_Heights ; 
8   dbpprop:mm [ dbpprop:name "Sunbittern" ] ; 
9   dbpprop:name "In the Wings" ; 
10  dbpprop:race <http://dbpedia.org/resource/Breeders%27_Cup_Turf>, 
11               dbpedia:Coronation_Cup, 
12               dbpedia:Grand_Prix_de_Saint-Cloud, 
13               dbpedia:Prix_Foy, 
14               <http://dbpedia.org/resource/Prix_du_Prince_d%27Orange> ; 
15  dbpprop:sex dbpedia:Stallion ; 
16  dbpprop:sire <http://dbpedia.org/resource/Sadler%27s_Wells_%28horse%29> ; 
17  dbpprop:trainer <http://dbpedia.org/resource/Andr%C3%A9_Fabre> ; 
18 ### ... 
19 . 
This excerpt, including all the properties you need to map, is found in the ontology in the accompanying file racehorse.owl and at the following address: 
http://sws.ifi.uio.no/inf3580/v14/oblig/6/racehorse 
Your mapping ontology should be a separate file and it should import the ontology at the above address from this address and additionally the ontology you have made in the first exercise. 

Notes: 
In the properties dbpprop:m, dbpprop:fm, dbpprop:mm, and so on, m means "mother" and f "father", so two letters means a grand-parent, e.g., dbpprop:fm is the mother to the father (norwegian: farmor) to the horse. 
In the excerpt dbpedia:Stallion is an individual (and not a class). 
If the intended meaning of the properties or other resources in the excerpt is not clear, use a reasonable interpretation you find fit. 
Since you will be working with resources from different ontologies, keeping them apart is smart. To display names in Protégé using qualified names enable the setting found in Protégé under the File -> Preferences -> Renderer -> "Render by qualified name". 
2.1 Questions 
Apply reasoning to your ontology and answer the following questions: 
1. List all stallions. 
2. List all male horses. 
3. Since "Northern Dancer" is an ancestor of "In the Wings", the ancestors of "Northern Dancer" should also be the ancestors of "In the Wings". Why is this not the case?

3 Other OWL 2 Features
3.1 Punning <- Do not answer
The official RDF semantics gives a meaning also to triples where subjects and objects can be classes or properties. This is not supported by the "DL" semantics however, and indeed, none of the reasoners connected to Protégé are able to deal with ontologies where individuals, classes, and properties are not clearly separated.
Still, it is possible to load such ontologies into Protégé, based on a mechanism called "punning," see http://www.w3.org/TR/owl2-new-features/ #F12:_Punning
Let Γ3 be the ontology listed below, using Manchester syntax for brevity. A turtle variant is listed in the appendix. 
ObjectProperty: member 
InverseOf: rdf:type 
Class: OrderOfAnimals 
Class: OrderOfMammals 
EquivalentTo: OrderOfAnimals and (member only Mammal) 
Class: Mammal 
Types: OrderOfMammals 
Class: Elephant 
SubClassOf: Mammal 
Individual: Bobo 
Types: Elephant 
An OrderOfMammals is an OrderOfAnimals whose members must be Mammal-s. Since Elephant is a subclass of Mammal, which is a (, i.e., has type) OrderOfMammals, one could expect that a DL reasoner would infer that Elephant is an OrderOfMammals. However, this is not the case. Explain why. 
3.2 Annotation properties 
In OWL, rdfs:label is a predefined annotation property, see http://www. w3.org/TR/owl-ref/#Annotations. Explain what an annotation property is and why they are useful. 

Good Luck! 
5 Appendix 
5.1 SPARQL mapping query 
This is the SPARQL query used to create the excerpt. 
1 DESCRIBE ?horse 
2 WHERE 
3 { 
4   ?horse dbpprop:horsename [] ; 
5          dbpprop:race [] . 
6   { ?horse dcterms:subject 
7            <http://dbpedia.org/resource/Category:Racehorses> } 
8   UNION 
9     { ?horse dcterms:subject 
10        [ skos:broader 
11          <http://dbpedia.org/resource/Category:Racehorses> ] } 
12 }
The result of this query (8MB) is found in the accompanying dbpedia-dump.rdf file  and at 
http://sws.ifi.uio.no/inf3580/v14/oblig/6/dbpedia-dump 
5.2 Punning Turtle file 
@prefix : <http://example.org#> . 
@prefix owl: <http://www.w3.org/2002/07/owl#> . 
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . 
@prefix xml: <http://www.w3.org/XML/1998/namespace> . 
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> . 
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . 
:member rdf:type owl:ObjectProperty ; 
owl:inverseOf rdf:type . 
:OrderOfAnimals rdf:type owl:Class . 
:OrderOfMammals rdf:type owl:Class ; 
owl:equivalentClass [ rdf:type owl:Class ; 
owl:intersectionOf 
( :OrderOfAnimals 
      [ rdf:type owl:Restriction ;         
        owl:onProperty :member ;   
        owl:allValuesFrom :Mammal ] ) ] . 
:Mammal rdf:type :OrderOfMammals . 
:Elephant rdfs:subClassOf :Mammal . 
:Bobo rdf:type :Elephant . 