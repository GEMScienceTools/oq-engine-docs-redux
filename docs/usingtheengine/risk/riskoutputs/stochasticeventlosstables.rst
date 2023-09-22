Stochastic Event Loss Tables
============================

The asset loss table
--------------------

When performing an event based risk calculation the engine keeps in memory a table with the losses for each asset and 
each event, for each loss type. It is usually impossible to fully store such a table, because it is extremely large; 
for instance, for 1 million assets, 1 million events, 2 loss types and 4 bytes per loss ~8 TB of disk space would be 
required. It is true that many events will produce zero losses because of the *maximum_distance* and *minimum_intensity* 
parameters, but still, the asset loss table is prohibitively large and for many years could not be stored. In engine 3.8 
we made a breakthrough: we decided to store a partial asset loss table, obtained by discarding small losses, by 
leveraging on the fact that loss curves for long enough return periods are dominated by extreme events, i.e. there is 
no point in saving all the small losses.

To that aim, the engine honours a parameter called ``minimum_asset_loss`` which determines how many losses are 
discarded when storing the asset loss table. The rule is simple: losses below ``minimum_asset_loss`` are discarded. By 
choosing the threshold properly in an ideal world

1. the vast majority of the losses would be discarded, thus making the asset loss table storable;
2. the loss curves would still be nearly identical to the ones without discarding any loss, except for small return periods.

It is the job of the user to verify if 1 and 2 are true in the real world. He can assess that by playing with the 
``minimum_asset_loss`` in a small calculation, finding a good value for it, and then extending it to the large 
calculation. Clearly, it is a matter of compromise: by sacrificing precision it is possible to reduce enormously the 
size of the stored asset loss table and to make an impossible calculation possible.

Starting from engine 3.11 the asset loss table is stored if the user specifies ``aggregate_by = id`` in the job.ini file. 
In large calculations it is extremely easy to run out of memory or make the calculation extremely slow, so we recommend 
not to store the asset loss table. The functionality is there for the sole purpose of debugging small calculations, for 
instance, to see the effect of the ``minimum_asset_loss`` approximation at the asset level.

For large calculations usually one is interested in the aggregate loss table, which contains the losses per event and 
per aggregation tag (or multi-tag). For instance, the tag ``occupancy`` has the three values “Residential”, “Industrial” 
and “Commercial” and by setting ``aggregate_by = occupancy`` the engine will store a pandas DataFrame called ``risk_by_event`` 
with a field ``agg_id`` with 4 possible value: 0 for “Residential”, 1 for “Industrial”, 2 for “Commercial” and 3 for 
the full aggregation.

NB: if the parameter ``aggregate_by`` is not specified, the engine will still compute the aggregate loss table but then 
the agg_id field will have a single value of 0 corresponding to the total portfolio losses.