Hazard Calculators
==================

The hazard component of the OpenQuake engine can compute seismic hazard using various approaches. Three types of 
analysis are currently supported:

- Classical Probabilistic Seismic Hazard Analysis (PSHA), allowing calculation of hazard curves and hazard maps following the classical integration procedure ((Cornell 1968), McGuire (1976)) as formulated by (Field, Jordan, and Cornell 2003).
- Event-Based Probabilistic Seismic Hazard Analysis, allowing calculation of ground-motion fields from stochastic event sets. Traditional results - such as hazard curves - can be obtained by post- processing the set of computed ground-motion fields.
- Scenario Based Seismic Hazard Analysis, allowing the calculation of ground motion fields from a single earthquake rupture scenario taking into account ground motion aleatory variability. The ground motion fields can be conditioned to observed data, when available.

Each workflow has a modular structure, so that intermediate results can be exported and analyzed. Each calculator can be 
extended independently of the others so that additional calculation options and methodologies can be easily introduced, 
without affecting the overall calculation workflow.


.. toctree::
   :maxdepth: 1
   :hidden:

   classicalpsha
   stochasticeventbasedpsha
   scenariobasedsha
   seismichazarddisaggregation
