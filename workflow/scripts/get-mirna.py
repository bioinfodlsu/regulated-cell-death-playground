import argparse


def get_mrna_in_file(mrna_list):
    mrna = set()
    with open(mrna_list) as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                mrna.add(line.strip())

    return mrna


def get_mirna(mrna, mirdb, output):
    with open(mirdb) as f, open(output, "w") as g:
        for line in f:
            line = line.strip().split("\t")
            if line[1] in mrna:
                # Convert to lowercase to match casing in TCGA
                mirna = line[0].lower()

                # Remove strand info
                if mirna.endswith("-5p") or mirna.endswith("-3p"):
                    mirna = mirna[: -len("-5p")]

                g.write(f"{mirna}\t{line[1]}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mrna-list",
        help="path to the text file containing the list of RefSeq gene IDs of the mRNAS of interest",
    )
    parser.add_argument(
        "--output",
        help="filename of text file containing the miRNAs targeting the given mRNAs",
    )
    parser.add_argument(
        "--mirdb",
        help="path to miRDB dataset",
        default="data/miRDB_v6.0_prediction_result.txt",
    )

    args = parser.parse_args()

    get_mirna(get_mrna_in_file(args.mrna_list), args.mirdb, args.output)
