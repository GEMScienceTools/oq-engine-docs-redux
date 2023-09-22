Motivation and Basics of the OpenQuake Engine
=============================================

This book aims to provide an explanation of the scientific basis and
the methodologies adopted in the implementation of the OpenQuake
engine, an open source code for seismic hazard and physical risk
calculation. The book follows the traditional openness and
transparency features of the **Global Earthquake Model (GEM)** as clearly
indicated in the development principles of the OpenQuake engine.

The **GEM** initiative is a global collaborative effort with the aim to
provide organisations and people with tools and resources for
transparent assessment of earthquake risk anywhere in the world. The
OpenQuake engine is a fully integrated, flexible and scalable hazard
and physical risk calculation engine whose development is at the core
of **GEM**’s overall objectives.

Basics of the Engine
--------------------

The implementation of the OpenQuake software officially started in
Summer 2010 following the experience gained in **GEM**’s kick-off project
GEM1 [*GEM Foundation, 2010*], during which an extensive appraisal of
existing hazard and physical risk codes was performed [*Danciu et al.,
2010; Crowley et al., 2010b*] and prototype hazard and risk software
were selected, designed and implemented [*Pagani et al., 2010; Crowley
et al., 2010a*].

The current version of the OpenQuake engine is Python code developed
following the most common requirements of Open Source software
development, such as a public repository, IRC channel and open
mailing lists. The source code, released under an open source
software license, is freely and openly accessible on a web based
repository (see `github.com/gem <http://github.com/gem>`__) while the
development process is managed so that the community can participate
to the day by day development as well as in the mid- and long-term
design process. The software development also leverages on a number
of open source projects such as `Celeryd <http://celeryproject.org/>`__ and
`RabbitMQ <http://www.rabbitmq.com/>`__, just to mention a few.

The hazard component of the engine largely relies on classes
belonging to the OpenQuake Hazard library (see
`oq-hazardlib <https://github.com/gem/oq-hazardlib>`__) a
comprehensive library for performing state-of-the-art PSHA. This
library has been designed and implemented following the successful
collaboration and important lessons learnt working with the
`OpenSHA <http://www.opensha.org/>`__ software and the developing
teams at **United States Geological Survey (USGS)** and **Southern
California Earthquake Center (SCEC)** in GEM1. The risk component of
the engine was designed in GEM1, prototyped in Java and eventually
coded in Python by the team operating at the **GEM** Model Facility.
This scientific code was originally integrated with the engine, but
in late 2012 it was extracted to form the OpenQuake Risk Library (see
`oq-risklib <https://github.com/gem/oq-risklib>`__).

Structure of the Book
---------------------

The OpenQuake Engine Book is organized into two volumes, one which
describes the science behind the hazard component of the engine and
another which illustrates the theory of the physical risk calculators
incorporated into the software. Readers that are interested in
learning how to run calculations using the OpenQuake engine are
referred to the OpenQuake Engine User Manual.

The GEM Hazard Team is currently updating the volume on hazard. In
the meantime, interested readers are referred to the OpenQuake
Engine User Manual, or they can contact the coordinator, Dr. Marco
Pagani, for further information.

This volume on risk is organised as follows:

- Chapter **2** introduces the main physical risk concepts and workflows.

- Chapter **3** contains an explanation of the exposure, physical vulnerability 
  and fragility concepts, which are input to the calculations.

- Chapter **4** describes the scenario risk methodology, for estimating loss 
  distributions for single events.

- Chapter **5** describes the scenario damage methodology, for estimating 
  damage ditributions for single events.

- Chapter **6** provides an overview of the probabilistic event-based risk 
  calculation methodology, which produces loss exceedance curves for portfolios 
  of buildings.

- Chapter **7** illustrates single-asset risk calculations based on the hazard 
  curves from classical PSHA.

- Chapter **8** outlines the benefit/cost ratio calculations based on loss curves 
  for structures with and without retrofitting.