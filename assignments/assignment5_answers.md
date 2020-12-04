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

# 2 Exercise: Mapping DBpedia to your ontology 

The task of this exercise is to create a mapping of parts of the DBpedia vocabulary about horses and racehorses to your ontology from the exercise above. 

Below is an excerpt from the result of running a DESCRIBE query on the dbpedia.org SPARQL endpoint: http://dbpedia.org/sparql. The excerpt contains data about two racehorses, one of them is listed below, a racehorse called "In the Wings". The exercise is to create a mapping ontology that maps all properties mentioned in the excerpt to the ontology you created in the exercise above.

The mapping shall be created by giving a series of axioms (i.e., sub- class/property and equivalence axioms) which relate the dbpedia properties to your classes and properties, e.g, 

dbpprop:dam owl:equivalentProperty :dam 

creates a mapping between the dbpprop:dam and "your" :dam property.

Note that the left-hand-side and right-hand-side of axioms can be complex classes or properties, e.g., dbpprop:horsename should be mapped to some combination of :name and :Horse (not only to :name) (Tip: you need to use the general class axioms feature in Protégé to express this.) 

- I've tried dbp:horsename EquivalentTo: name and rdfs:type Horse for this, but it did not work

Note the owl:equivalentProperty relation only applies to lists of properties:
axiom ::= 'EquivalentProperties(' URIreference URIreference  { URIreference } ')' ...


Your mapping ontology should be a separate file and it should import the ontology at the above address from this address and additionally the ontology you have made in the first exercise. 

Notes: 
In the properties dbpprop:m, dbpprop:fm, dbpprop:mm, and so on, m means "mother" and f "father", so two letters means a grand-parent, e.g., dbpprop:fm is the mother to the father (norwegian: farmor) to the horse.

In the excerpt dbpedia:Stallion is an individual (and not a class). 

If the intended meaning of the properties or other resources in the excerpt is not clear, use a reasonable interpretation you find fit. 

Since you will be working with resources from different ontologies, keeping them apart is smart. To display names in Protégé using qualified names enable the setting found in Protégé under the File -> Preferences -> Renderer -> "Render by qualified name". 
## 2.1 Questions 
Apply reasoning to your ontology and answer the following questions: 
### 1. List all stallions. 

"In the Wings", "Northern Dancer"  (that we know of)

### 2. List all male horses. 

"In the Wings", "Northern Dancer" (that we know of)

### 3. Since "Northern Dancer" is an ancestor of "In the Wings", the ancestors of "Northern Dancer" should also be the ancestors of "In the Wings". Why is this not the case?

The information of " "Northern Dancer" is an ancestor of "In the Wings" " is not asserted and cannot be inferred from the ontology.

# 3.2 Annotation properties 
## In OWL, rdfs:label is a predefined annotation property, see http://www.w3.org/TR/owl-ref/#Annotations. Explain what an annotation property is and why they are useful. 

Annotation properties are properties that serve to add extra information to parts of the ontology. Accorging to the OWL 2 syntax descriptor (https://www.w3.org/TR/owl2-syntax/#Annotation_Properties),  "Annotation properties can be used to provide an annotation for an ontology, axiom, or an IRI."

They have many use cases. "rdfs:label" can provide human readable labels, and "rdfs:comment" can provide human readable comments. More generally, they guide human readers in understanding the details of the design choices and ontological commitments, and help to clarify concepts. As they are a structured part of the ontology (in contrast with code comments) they can be read and dealt with by user interfaces like Protege. 

