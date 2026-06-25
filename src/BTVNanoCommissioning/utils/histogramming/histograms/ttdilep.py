import hist as Hist


def get_histograms(axes, **kwargs):
    hists = {}

    for i in range(2):
        hists[f"dr_mujet{i}"] = Hist.Hist(
            axes["syst"], axes["flav"], axes["dr"], Hist.storage.Weight()
        )

    for i in ["mu", "ele"]:
        if i == "mu":
            hists[f"{i}_pfRelIso04_all"] = Hist.Hist(
                axes["syst"], axes["iso"], Hist.storage.Weight()
            )
        else:
            hists[f"{i}_pfRelIso03_all"] = Hist.Hist(
                axes["syst"], axes["iso"], Hist.storage.Weight()
            )
        hists[f"{i}_dxy"] = Hist.Hist(axes["syst"], axes["dxy"], Hist.storage.Weight())
        hists[f"{i}_dz"] = Hist.Hist(axes["syst"], axes["dz"], Hist.storage.Weight())

        """
        # 2D correlation study
        hists[f"{i}pt_vs_firstjetpt"] = Hist.Hist(
            axes["syst"],
            axes["flav"],
            Hist.axis.Regular(60, 0, 300, name="leppt", label=" $p_{T}$ [GeV]"),
            Hist.axis.Regular(60, 0, 300, name="jetpt", label=" $p_{T}$ [GeV]"),
            Hist.storage.Weight(),
        )
        hists[f"{i}pt_vs_secondjetpt"] = Hist.Hist(
            axes["syst"],
            axes["flav"],
            Hist.axis.Regular(60, 0, 300, name="leppt", label=" $p_{T}$ [GeV]"),
            Hist.axis.Regular(60, 0, 300, name="jetpt", label=" $p_{T}$ [GeV]"),
            Hist.storage.Weight(),
        )
        """

    hists["top_pt"] = Hist.Hist(axes["syst"], axes["jpt"], Hist.storage.Weight())
    hists["antitop_pt"] = Hist.Hist(axes["syst"], axes["jpt"], Hist.storage.Weight())

    return hists
