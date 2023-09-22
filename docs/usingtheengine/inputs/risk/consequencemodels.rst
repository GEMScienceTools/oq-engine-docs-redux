Consequence Models
==================

Starting from OpenQuake engine v1.7, the Scenario Damage calculator also accepts consequence models in addition to 
fragility models, in order to estimate consequences based on the calculated damage distribution. The user may provide 
one *Consequence Model* file corresponding to each loss type (amongst structural, nonstructural, contents, and business 
interruption) for which a *Fragility Model* file is provided. Whereas providing a *Fragility Model* file for at least one 
loss type is mandatory for running a Scenario Damage calculation, providing corresponding *Consequence Model* files is 
optional.

This section describes the schema currently used to store consequence models, which are optional inputs for the Scenario 
Damage Calculator. A *Consequence Model* defines a set of consequence functions, describing the distribution of the loss 
(or consequence) ratio conditional on a set of discrete limit (or damage) states. These *Consequence Function* can be 
currently defined in OpenQuake engine by specifying the parameters of the continuous distribution of the loss ratio for 
each limit state specified in the fragility model for the corresponding loss type, for each taxonomy defined in the 
exposure model.

An example *Consequence Model* is shown in the listing below.::

	<?xml version="1.0" encoding="UTF-8"?>
	<nrml xmlns="http://openquake.org/xmlns/nrml/0.5">
	
	<consequenceModel id="consequence_example"
	                  assetCategory="buildings"
	                  lossCategory="structural">
	
	  <description>Consequence Model Example</description>
	  <limitStates>slight moderate extensive complete</limitStates>
	
	  <consequenceFunction id="RC_LowRise" dist="LN">
	    <params ls="slight" mean="0.04" stddev="0.00"/>
	    <params ls="moderate" mean="0.16" stddev="0.00"/>
	    <params ls="extensive" mean="0.32" stddev="0.00"/>
	    <params ls="complete" mean="0.64" stddev="0.00"/>
	  </consequenceFunction>
	
	</consequenceModel>
	
	</nrml>

The initial portion of the schema contains general information that describes some general aspects of the *Consequence 
Model*. The information in this metadata section is common to all of the functions in the *Consequence Model* and needs 
to be included at the beginning of every *Consequence Model* file. The parameters are described below:

- ``id``: a unique string used to identify the *Consequence Model*. This string can contain letters (a–z; A–Z), numbers (0–9), dashes (-), and underscores (_), with a maximum of 100 characters.
- ``assetCategory``: an optional string used to specify the type of assets for which consequencefunctions will be defined in this file (e.g: buildings, lifelines).
- ``lossCategory``: mandatory; valid strings for this attribute are “structural”, “nonstructural”, “contents”, and “business_interruption”.
- ``description``: mandatory; a brief string (ASCII) with further information about the *Consequence Model*, for example, which building typologies are covered or the source of the functions in the *Consequence Model*.
- ``limitStates``: mandatory; this field is used to define the number and nomenclature of each limit state. Four limit states are employed in the example above, but it is possible to use any number of discrete states. The limit states must be provided as a set of strings separated by white spaces between each limit state. Each limit state string can contain letters (a–z; A–Z), numbers (0–9), dashes (-), and underscores (_). Please ensure that there is no white space within the name of any individual limit state. The number and nomenclature of the limit states used in the *Consequence Model* should match those used in the corresponding *Fragility Model*.::

	<consequenceModel id="consequence_example"
	                  assetCategory="buildings"
	                  lossCategory="structural">
	
	  <description>Consequence Model Example</description>
	  <limitStates>slight moderate extensive complete</limitStates>

The following snippet from the above *Consequence Model* example file defines a *Consequence Function* using a lognormal 
distribution to model the uncertainty in the consequence ratio for each limit state::

	  <consequenceFunction id="RC_LowRise" dist="LN">
	    <params ls="slight" mean="0.04" stddev="0.00"/>
	    <params ls="moderate" mean="0.16" stddev="0.00"/>
	    <params ls="extensive" mean="0.32" stddev="0.00"/>
	    <params ls="complete" mean="0.64" stddev="0.00"/>
	  </consequenceFunction>

The following attributes are needed to define a *Consequence Function*:

- ``id``: mandatory; a unique string used to identify the taxonomy for which the function is being defined. This string is used to relate the *Consequence Function* with the relevant asset in the *Exposure Model*. This string can contain letters (a–z; A–Z), numbers (0–9), dashes (-), and underscores (_), with a maximum of 100 characters.
- ``dist``: mandatory; for vulnerability function which use a continuous distribution to model the uncertainty in the conditional loss ratios, this attribute should be set to either ``“LN”`` if using the lognormal distribution, or to ``“BT”`` if using the Beta distribution [1]_.
- ``params``: mandatory; this field is used to define the parameters of the continuous distribution used for modelling the uncertainty in the loss ratios for each limit state for this *Consequence Function*. For a lognormal distrbution, the two parameters required to specify the function are the mean and standard deviation of the consequence ratio. These parameters are defined for each limit state using the attributes ``mean`` and ``stddev`` respectively. The attribute ``ls`` specifies the limit state for which the parameters are being defined. The parameters for each limit state must be provided on a separate line. The number and names of the limit states in each *Consequence Function* must be equal to the number of limit states defined in the corresponding *Fragility Model* using the attribute ``limitStates``.

.. [1] Note that as of OpenQuake engine v1.8, the uncertainty in the consequence ratios is ignored, and only the mean consequence ratios for the set of limit states is considered when computing the consequences from the damage distribution. Consideration of the uncertainty in the consequence ratios is planned for future releases of the OpenQuake engine.