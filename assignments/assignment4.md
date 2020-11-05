# OWL

## Read
• Semantic Web Programming: chapter 4, 5
• Foundations of Semantic Web Technologies: chapter 4, 5.
## Supplementary reading:

• OWL Pizzas: Practical Experience of Teaching OWL-DL:Common Errors & Common Patterns

Now we will take our family ontology one step further by adding more
semantics using OWL. First, for a soft start and to get into Protégé, ontology
editing and OWL, we will start by looking at an existing tutorial ontology,
the pizza ontology. Parts of this exercise will be a revisit of first week’s
exercise.

# The Pizza ontology

The pizza ontology is a well-known ontology in the semantic web community.
It is developed for educational purposes by the University of Manchester,
which is a leading university in the development of semantic technologies.

The pizza ontology and a tutorial that uses it is found at
• http://protegewiki.stanford.edu/wiki/Protege4Pizzas10Minutes
• http://owl.cs.manchester.ac.uk/publications/talks-and-tutorials/
protg-owl-tutorial/

The tutorial is primarily for learning how to use Protégé 4. Use it to get
help on how to use Protégé in the coming exercises.

## Exercise 1.1

Open the pizza ontology in Protégé. Take some time to browse the class
hierarchy, the property hierarchies and the individuals and note how the
ontology describes the domain of pizzas.

## Exercise 1.2
Find Margherita and see how it is defined as a pizza with only cheese and
tomato topping. Look at the definition of VegetarianPizza. Is a Margherita
pizza a vegetarian pizza? Why / why not?

### Answer

- VegetarianPizza is defined as:
`Pizza
 and (not (hasTopping some SeafoodTopping))
 and (not (hasTopping some MeatTopping))`

as neither cheese or tomato toppings are subclasses of either SeafoodTopping or MeatTopping,
then  Margherita pizza is a vegetarian pizza.

## Exercise 1.3
Find hasIngredient. What is the domain and range of this property? What
are the subproperties of hasIngredient? What is the inverse property of
hasIngredient? What property characteristics does hasIngredient have?

### Answer

- Domain:
    - Food
- Ranges:
    - Food
- SubProperties:
    - hasBase
    - hasTopping
- Inverse Property:
    - isIngredientOf

Property characteristics:
rdfs:comment "NB Transitive - the ingredients of ingredients are ingredients of the whole"


## Exercise 1.4 
Classify the ontology by choosing a reasoner and then "classify" in the reasoner menu. In the "Inferred class hierarchy" two classes show up as subclasses of owl:Nothing. Answer the following questions:

• In general, what is the difference between the asserted class hierarchy
and the inferred class hierarchy?
• What does it mean for a class to be a subclass of owl:Nothing?
• Explain why these two classes appear as subclasses of owl:Nothing.
• Find Margherita in the inferred class hierarchy and see which classes
are inferred as superclasses of Margherita.

### Answer A

Asserted class hierarchies are explicitly added by editors. 
Inferred hierarchies stem from logical entailments derived from the asserted statements and the ontology constraints.

### Answer B

It means it does not have an assertion of subclass in the asserted hierarchy. 

### Answer C

They do not have an assertion of subclass in the asserted hierarchy. 

### Answer D

The HermiT reasoner inferred that Margherita is a subclass of CheesyPizza, VegetarianPizza1 and VegetarianPizza2 

## Exercise 1.5
Add a new class Grandiosa as a subclass of NamedPizza. Define "Grandiosa"
as something which
• hasTopping some HamTopping,
• hasTopping some TomatoTopping and
• hasTopping some CheeseTopping.
Classify the ontology. What superclasses are inferred as superclass of
Grandiosa? Explain why.

### Answer 
 The Elk reasoner inferred MeatyPizza and CheesyPizza as superclasses, due to "hasTopping some HamTopping" and "hasTopping some CheeseTopping" respectively. The HermiT reasoner inferred both previous superclasses and also InterestingPizza, as it has 3+ toppings.


## Exercise 1.6 
State in the ontology that a Grandiosa pizza comes from Norway, and that
Norway is different from the other countries already present in the pizza
ontology. Apply reasoning and explain the results.

### Answer 

The reasoner Hermit complained that the Individual Norway was outside the domain of the class country. The Elk reasoner did not show anything new. I changed the domain of Country and the HermiT reasoner did not show anything new. 

# Family relations in OWL

So far we have only been allowed to use RDFS vocabulary to describe family relations. Now we will extend our description using OWL constructs.

OWL is more expressive than RDFS and allows us to express many more
restrictions on properties and class membership than RDFS does.
In this exercise we will only use OWL (1) DL vocabulary (and not OWL
2, which will be next week’s exercises). This language is explained in W3C’s
OWL Web Ontology Language Reference, which may be a valuable resource
for these exercises. OWL Web Ontology Language Overview contains a list
of the constructs available in RDFS and the different dialects of OWL 1:
OWL lite, OWL DL and OWL Full. See also W3C’s "portal" on OWL.

You may use Protégé as your editor, but you are also welcome to use
a plain text editor to the exercises. Note that there are different OWL
languages and that different editors have different tastes. If you are using
Protégé as editor, consult the Protégé pizza tutorial. If your using a plain
text editor, use the OWL validator and try also regularly to open your file
in Protégé. If you have problems using Protégé, consult the Protégé OWL
Tutorial.

The OWL vocabulary we will use is listed below. The list is a slightly
compacted version of the one found on OWL Web Ontology Language
Overview. Almost all items in the list will be put to use in these exercises.
• RDFS Features: Class, rdfs:subClassOf, rdf:Property, rdfs:subPropertyOf,
rdfs:domain, rdfs:range, Individual
• Header Information: Ontology, imports
• Annotation Properties, rdfs:label, rdfs:comment, rdfs:seeAlso,
rdfs:isDefinedBy, AnnotationProperty, OntologyProperty
• Class Axioms: oneOf, dataRange, disjointWith, unionOf, complementOf,
intersectionOf
• (In)Equality: equivalentClass, equivalentProperty, sameAs, differentFrom,
AllDifferent, distinctMembers
• Property Characteristics: ObjectProperty, DatatypeProperty, inverseOf,
TransitiveProperty, SymmetricProperty, FunctionalProperty, InverseFunctionalProperty
• Property Restrictions: Restriction, onProperty, allValuesFrom,
someValuesFrom,
minCardinality, maxCardinality, cardinality, hasValue
• Datatypes: XSD datatypes
For each of the modelling exercises below express the exercise text as a
set of description logic (DL) axioms.

## Exercise 2.1
Make a new ontology file. Give it the namespace
http://www.ifi.uio.no/INF3580/v16/family.owl#
Import the family RDFS file you wrote in last week’s exercise.

## Tip 2.1.1
Note, as mentioned in an exercise in last week’s exercises, not all ontology
editors and reasoners interprets manages to handle RDFS as OWL, so you
might want to convert your family RDFS file to OWL. Changing all instances of rdfs:Class to owl:Class and instances of rdf:Propery to either
owl:ObjectProperty or owl:DatatypeProperty should take care of most
convertion problems.

# Exercise 2.2
State that a person has at least one father and one mother.

## Tip 2.2.1
The exercises are formulated in normal language on purpose. It is up to you
to decide how this is best expressed in OWL.

## Tip 2.2.2
My solution (yours may be different) as a DL axiom:
Person v ∃hasF ather.P erson u ∃hasMother.P erson

## Exercise 2.3
State that a person can only have one mother and only one father.

## Exercise 2.4
State that a woman can only have female as gender, and a man can only
have male as gender.

## Exercise 2.5
State that nothing can be both male and female.

## Exercise 2.6
Define the gender so that there can only be the genders man and woman.

## Exercise 2.7
Explain what disjointness is. For all pair of classes in the family ontology,
add the correct disjoint axioms.

## Exercise 2.8
State that a person is either a man or a woman, but not both.

## Exercise 2.9
Explain what inverse properties are. For all the properties that exist in our
ontology, add the correct inverse property axioms. You are not supposed
to add new properties, only state that a property is the inverse of an other
property if they already exist in the ontology.

## Exercise 2.10
Explain what it means for a property to be transitive or symmetric.
For all the properties in our ontology, if it is natural, state that they are
transitive and/or symmetric.
There is no standard way of asserting characteristics for properties in
DL, so you may skip this part. The more or less common way of assering
that a property P is asymmetric, symmetric, reflexive, reflexive or transitive
in DL literature is Asym(P), Sym(P), Ref(P), Irr(P) or Tra(P), respectively.
To say that two properties P1 and P2 are disjoint is commonly done in
DL literature with Dis(P1, P2).

## Exercise 2.11
Is a subproperty of a transitive property necessarily also transitive? Explain
why / why not?

## Exercise 2.12
Is a subproperty of a symmetric property necessarily also symmetric? Explain why / why not?

## Exercise 2.13
Explain what it means for a property to be inverse functional.
For all properties in our ontology, state that they are inverse functional
if you believe that is correct.