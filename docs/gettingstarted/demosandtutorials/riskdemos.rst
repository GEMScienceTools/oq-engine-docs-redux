Demonstrative Examples for Risk Module
======================================

The following sections describe the set of demos that have been compiled to demonstrate some of the features and usage of 
the risk calculators of the OpenQuake engine. These demos can be found in a public repository on GitHub at the following 
link: `gem/oq-engine <https://github.com/gem/oq-engine/tree/master/demos/risk>`_.

These examples are purely demonstrative and are not intended to represent accurately the seismicity, vulnerability or 
exposure characteristics of the region selected, but simply to provide example input files that can be used as a starting 
point for users planning to employ the OpenQuake engine in seismic risk and loss estimation studies.

It is also noted that in the demonstrative examples presented in this section, illustrations about the various messages 
from the engine displayed in the command line interface are presented. These messages often contain information about the 
calculation id and output id, which will certainly be different for each user.

Following is the list of demos which illustrate how to use the OpenQuake engine for various scenario-based and 
probabilistic seismic damage and risk analyses:

- ClassicalBCR
- ClassicalDamage
- ClassicalRisk
- EventBasedDamage
- EventBasedRisk
- ScenarioDamage
- ScenarioRisk

These seven demos use Nepal as the region of interest. An example Exposure Model has been developed for this region, 
comprising 9,063 assets distributed amongst 2,221 locations (due to the existence of more than one asset at the same 
location). A map with the distribution of the number of buildings throughout Nepal is presented in :ref:`Fig. 1.12 <Fig. 1.12>`.

.. _Fig. 1.12:
.. figure:: _images/exposure-nepal.png

   Fig. 1.12 Distribution of number of buildings in Nepal

The building portfolio was organised into four classes for the rural areas (adobe, dressed stone, unreinforced fired 
brick, wooden frames), and five classes for the urban areas (the aforementioned typologies, in addition to reinforced 
concrete buildings). For each one of these building typologies, vulnerabilityfunctions and fragilityfunctions were 
collected from the published literature available for the region. These input models are only for demonstrative purposes 
and for further information about the building characteristics of Nepal, users are advised to contact the National 
Society for Earthquake Technology of Nepal (NSET - http:www.nset.org.np/).

The following sections include instructions not only on how to run the risk calculations, but also on how to produce the 
necessary hazard inputs. Thus, each demo comprises the configuration file, *Exposure Model* and fragility or vulnerability 
models fundamental for the risk calculations. Each demo folder also a configuration file and the input models to produce 
the relevant hazard inputs.

Scenario Damage
---------------

Demos A rupture of magnitude Mw 7 in the central part of Nepal is considered in this demo. The characteristics of this 
rupture (geometry, dip, rake, hypocentre, upper and lower seismogenic depth) are defined in the ``fault_rupture.xml`` 
file, and the hazard and risk calculation settings are specified in the ``job.ini`` file.

To run the Scenario Damage demo, users should navigate to the folder where the required files have been placed and employ 
following command::

	user@ubuntu:~$ oq engine --run job_hazard.ini && oq engine --run job_risk.ini --hc=-1

The hazard calculation should produce the following outputs::

	Calculation 8967 completed in 4 seconds. Results:
	  id | name
	9060 | Ground Motion Fields
	9061 | Realizations

and the following outputs should be produced by the risk calculation::

	Calculation 8968 completed in 16 seconds. Results:
	  id | name
	9062 | Average Asset Damages
	9063 | Average Asset Losses

Scenario Risk Demos
-------------------

The same rupture described in the Scenario Damage demo is also used for this demo. In this case, a combined job file, 
job.ini, is used to specify the configuration parameters for the hazard and risk calculations.

To run the Scenario Risk demo, users should navigate to the folder where the required files have been placed and employ 
following command::

	user@ubuntu:~$ oq engine --run job.ini

and the following outputs should be produced::

	Calculation 8970 completed in 16 seconds. Results:
	  id | name
	9071 | Aggregate Asset Losses
	9072 | Full Report
	9073 | Ground Motion Fields
	9074 | Average Asset Losses
	9075 | Aggregate Event Losses
	9076 | Realizations

.. _classical-psda-demo:

Classical Probabilistic Seismic Damage Demos
--------------------------------------------

The seismic source model developed within the Global Seismic Hazard Assessment Program (GSHAP) is used with the 
(B. S.-J. Chiou and Youngs 2008) ground motion prediction equation to produce the hazard input for this demo. No 
uncertainties are considered in the seismic source model and since only one GMPE is being considered, there will be only 
one possible path in the logic tree. Therefore, only one set of seismic hazard curves will be produced. To run the hazard 
calculation, the following command needs to be employed::

	oq engine --run job_hazard.ini

which will produce the following sample hazard output::

	Calculation 8971 completed in 34 seconds. Results:
	  id | name
	9074 | Hazard Curves
	9075 | Realizations

The risk job calculates the probabilistic damage distribution for each asset in the *Exposure Model* starting from the 
above generated hazard curves. The following command launches the risk calculations::

	user@ubuntu:~$ oq engine --run job_risk.ini --hc 8971

and the following sample outputs are obtained::

	Calculation 8972 completed in 16 seconds. Results:
	  id | name
	9076 | Asset Damage Distribution
	9077 | Asset Damage Statistics

Classical Probabilistic Seismic Risk Demos
------------------------------------------

The same hazard input as described in the Classical Probabilistic Damage demo is used for this demo. Thus, the workflow 
to produce the set of hazard curves described in Section :ref:`Classical Probabilistic Seismic Damage Demos <classical-psda-demo>` 
is also valid herein. Then, to run the Classical Probabilistic Risk demo, users should navigate to the folder containing 
the demo input models and configuration files and employ the following command::

	user@ubuntu:~$ oq engine --run job_hazard.ini

which will produce the following hazard output::

	Calculation 8971 completed in 34 seconds. Results:
	  id | name
	9074 | Hazard Curves
	9075 | Realizations

In this demo, loss exceedance curves for each asset and two probabilistic loss maps (for probabilities of exceedance of 
1% and 10%) are produced. The following command launches these risk calculations::

	user@ubuntu:~$ oq engine --run job_risk.ini --hc 8971

and the following outputs are expected::

	Calculation 8973 completed in 16 seconds. Results:
	  id | name
	9077 | Asset Loss Curves Statistics
	9078 | Asset Loss Maps Statistics
	9079 | Average Asset Loss Statistics

Event Based Probabilistic Seismic Damage Demos
----------------------------------------------

This demo uses the same probabilistic seismic hazard assessment (PSHA) model described in the previous examples in 
Section Classical Probabilistic Seismic Damage Demos and Section Classical Probabilistic Seismic Risk Demos. However, 
instead of hazard curves, sets of ground motion fields will be generated by the hazard calculation of this demo. Again, 
since there is only one Branch in the logic tree, only one set of ground motion fields will be used in the risk 
calculations. The hazard and risk jobs are defined in a single configuration file for this demo. To trigger the hazard 
and risk calculations the following command needs to be used::

	user@ubuntu:~$ oq engine --run job.ini

and the following results are expected::

	Calculation 2 completed in 29 seconds. Results:
	  id | name
	  24 | Aggregate Event Damages
	  30 | Aggregate Event Losses
	  20 | Average Asset Damages
	  21 | Average Asset Damages Statistics
	  22 | Average Asset Losses
	  23 | Average Asset Losses Statistics
	  32 | Earthquake Ruptures
	  25 | Events
	  26 | Full Report
	  27 | Ground Motion Fields
	  28 | Hazard Curves
	  29 | Input Files
	  31 | Realizations

Event Based Probabilistic Seismic Risk Demos
--------------------------------------------

This demo uses the same probabilistic seismic hazard assessment (PSHA) model described in the previous examples in 
Section Classical Probabilistic Seismic Damage Demos and Section Classical Probabilistic Seismic Risk Demos. However, 
instead of hazard curves, sets of ground motion fields will be generated by the hazard calculation of this demo. Again, 
since there is only one Branch in the logic tree, only one set of ground motion fields will be used in the risk 
calculations. The hazard and risk jobs are defined in a single configuration file for this demo. To trigger the hazard 
and risk calculations the following command needs to be used::

	user@ubuntu:~$ oq engine --run job.ini

and the following results are expected::

	Calculation 8974 completed in 229 seconds. Results:
	  id | name
	1820 | Total Loss Curves
	1821 | Total Loss Curves Statistics
	1822 | Aggregate Loss Table
	1823 | Average Asset Losses
	1824 | Average Asset Loss Statistics
	1826 | Asset Loss Maps
	1827 | Asset Loss Maps Statistics
	1828 | Average Asset Losses
	1829 | Average Asset Losses Statistics
	1830 | Earthquake Ruptures
	1831 | Events
	1832 | Realizations

The number and the name of the outputs can change between different versions of the engine.

Retrofit Benefit-Cost Ratio Demos
---------------------------------

The loss exceedance curves used within this demo are produced using the Classical Probabilistic Risk calculator. Thus, 
the process to produce the seismic hazard curves described in Section Classical Probabilistic Seismic Risk Demos can be 
employed here. Then, the risk calculations can be initiated using the following command::

	oq engine --run job_risk.ini --hc 8971

which should produce the following output::

	Calculation 8976 completed in 14 seconds. Results:
	  id | name
	9087 | Benefit Cost Ratios