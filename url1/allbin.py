from room import app
from room import db
from models import ParadeMiis


@app.route("/url1/special/allbin.xml")
def allbin():
    # Yes, I know this has a lot of work to go. I will to most of that later.
    query = ParadeMiis.query.all()
    # Now that we have a query, we grab our values
    mii_ids = []
    logo_ids = []
    logo_bins = []
    mii_bins = []
    # These are populated by this next loop
    for i in query:
        mii_ids.append(i.miiid)
        logo_ids.append(i.logo1id)
        logo_bins.append(i.logobin)
        mii_bins.append(i.miibin)
        # Return all of that in XML form
        # Currently very bad lol
    base = """
<SpPageBin>
    <ver>399</ver>
    {content}
</SpPageBin>
    """
    # Currently, having more than like 2 miis makes it too big for a string
    content = ""
    for mii_id, logo_id, logo_bin, mii_bin in mii_ids, logo_ids, logo_bins, mii_bins:
        content = (
            content
            + """
<bininfo>
    <sppageid>{mii_id}</sppageid>
    <miiid>{mii_id}</miiid>
    <logo1id>{logo_id}</logo1id>
    <miibin>{mii_bin}</miibin>
    <logobin>{logo_bin}</logobin>
</bininfo>
""".format(
                mii_id=mii_id, logo_id=logo_id, mii_bin=mii_bin
            )
        )
    return base.format(content=content)
