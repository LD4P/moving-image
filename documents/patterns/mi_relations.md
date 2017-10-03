# Moving image relations

## Recommendation overview
The LD4L/LD4P core ontology paper [Relations](https://docs.google.com/document/d/1SU4VqY-T8sh3WHIfkKZaj2SpOzjlgOZE56F1NpGMmaM/edit#heading=h.9tzj15vuofrj) recommends the use of unconstrained RDA properties to describe derivative and equivalence relationships between work and/or instance entities in BIBFRAME, and BF 2.0 properties to describe other content relationships. Following that recommendation, this paper specifies some properties of particular relevance in relating moving image works and proposes relationships with commonly-used external identifiers as an additional way to create relationships between works through querying or inference.

## Related documents
Relations
Identifiers

## Approach to moving forward

![diagram of relationships](https://github.com/LD4P/moving-image/blob/develop/documents/patterns/mi_relations.svg)

* Following a LD4L/P core ontology recommendation, use unconstrained RDA properties to relate works and their derivatives, including:
  * rdau:60710 “has derivative resource relationship with” where directionality is unclear
  * rdau:60223 “is abridgement of”
    * Mint new subproperty mi:isCensoredVersionOf
  * rdau:60294 “is expanded version of”
  * rdau:60303 “is revision of”
* Furthermore, use rdau:P60713 ("has sequential resource relationship with") and its subproperties to describe sequential content relationships
  * rdau:P60577 "is sequel to" and rdau:P60102 “is sequel”
  * rdau:P60310 “is prequel to” and rdau:P60220 “is prequel”
* Use dcterms:subject to relate trailers (or other works about works) to works
* Use bf:hasExpression and bf:expressionOf to relate works to other versions of the same work
* Use bf:identifiedBy to relate works to identifiers and use shared identifiers to infer relationships between works
  * Mint mi:ImdbNumber as a subclass of bf:Identifier, and consider minting new subclasses of bf:Identifier as needed for other identifers
  * As an experiment, automatically generate a work entity for each IMDB number used in descriptions, and generate expression relationships between these works and described works based on shared identifiers (see diagram)

## Involved properties

bf:expressionOf
Label: Expression of
URI: http://id.loc.gov/ontologies/bibframe/expressionOf
Definition: Work that the described Work is an expression of. For use to connect Works under FRBR/RDA rules.
SubProperty Of:  http://id.loc.gov/ontologies/bibframe/relatedTo
Used with: http://id.loc.gov/ontologies/bibframe/Work

bf:hasExpression
Label: Expression of
URI: http://id.loc.gov/ontologies/bibframe/hasExpression
Definition: 
SubProperty Of:  http://id.loc.gov/ontologies/bibframe/relatedTo
Used with: http://id.loc.gov/ontologies/bibframe/Work

bf:identifiedBy 
Label: Identifier
URI: http://id.loc.gov/ontologies/bibframe/identifiedBy
Definition: Character string associated with a resource that serves to differentiate that resource from other resources, i.e., that uniquely identifies an entity.
Comment: Used with Unspecified
Domain: unspecified
Range: bf:Identifier
Inverse: http://id.loc.gov/ontologies/bibframe/identifies

bf:identifies 
Label: identifies
URI: http://id.loc.gov/ontologies/bibframe/identifies
Definition: Resource that this character string serves to differentiate that resource from other resources, i.e., that uniquely identifies an entity.
Domain: bf:Identifier
Range: unspecified
Inverse: http://id.loc.gov/ontologies/bibframe/identifiedBy

rdau:60710 
label: has derivative resource relationship with
URI: http://rdaregistry.info/Elements/u/P60305
definition: Relates a resource to a resource that is based on or is a derivative of another resource.
Subproperties:
rdau:P60250 “is derivative”
rdau:P60305 “is based on”

rdau:P60250
Label: is derivative
URI: http://rdaregistry.info/Elements/u/P60250
Definition: Relates a resource to a resource that is a modification of a source resource.
Subproperty of: http://rdaregistry.info/Elements/u/P60305
Subproperties include: 
rdau:P60120 "is remade as"
rdau:P60245 "is revised as"
rdau:P60260 "is adapted as"
rdau:P60275 "is abridged as"

rdau:P60305
Label: is based on
URI: http://rdaregistry.info/Elements/u/P60305
Definition: Relates a resource to a resource used as the source for a derivative resource.
Subprpoperty of: http://rdaregistry.info/Elements/u/P60305
Subproperties include:
rdau:P60223 "is abridgement of"
rdau:P60241 "is adaptation of"
rdau:P60294 "is expanded version of"
rdau:P60295 "is remake of"
rdau:P60303 "is revision of"
rdau:P60713 "has sequential resource relationship with"
rdau:P60577 "is sequel to" 
rdau:P60102 “is sequel”
rdau:P60310 “is prequel to”
rdau:P60220 “is prequel”

dcterms:subject
label: subject
URI: http://purl.org/dc/terms/subject
Definition: The topic of the resource.

mi:isCensoredVersionOf
label: is censored version of
Subprpoperty of: http://rdaregistry.info/Elements/u/P60223
URI: tbd

mi:isCensoredAs
label: is censored as
Subprpoperty of: http://rdaregistry.info/Elements/u/P60305
URI: tbd

Involved classes
bf:Identifier
Label: Identifier
URI: http://id.loc.gov/ontologies/bibframe/Identifier
Definition: Token or name that is associated with a resource, such as a URI or an ISBN.
Comment: Used with Unspecified

mi:ImdbNumber
Label: IMDB number
URI: tbd
Subclass of: http://id.loc.gov/ontologies/bibframe/Identifier 

## Local use cases
* Trailers
* Short versions
* Parts
* Censored versions
* Revised versions
* Sequels/prequels

Taxi Driver: as example for everything ever, but especially trailers and condensed version
Five Year Diary (Anne Robertson): parts, sequences
Warming of Hell House (and other Kuchar works): revised versions
Peeping Tom (Powell & Pressburger): censored versions
Sequels/prequels: Star Wars
Mapping to local metadata

Filemaker data does not express relationships between records in any structured or consistent way

## Discussion
Is this an actual use case for this baffling rdau property? http://www.rdaregistry.info/Elements/u/#P60710
Its subproperties include some that wouldn’t relate expressions of the same imdb-esque work
For expressions identified with the same IMDB number, automatically assert that they share a frbresque work with no title, etc, but links to external descriptions 
For expressions that are expressions of each other or derived from each other, automatically assert that they share a frbresque work with no title, etc, but links to external descriptions 
Which properties, specifically?
bf:hasExpression
bf:expressionOf 
Do we need a third, symmetric, catch-all property?
Not trailers, not bf:relatedTo

Consider creating a property that means “these are siblings that are expressions of the same work” without implying direction/sequence
