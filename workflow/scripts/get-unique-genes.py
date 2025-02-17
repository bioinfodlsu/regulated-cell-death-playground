import argparse
import csv
import os


def get_rcd_type(rcd_file):
    return rcd_file.split("/")[-1][: -len(".csv")]


def make_dict_of_genes(rcd_file):
    dict_of_genes = {}
    with open(rcd_file) as f:
        handle = csv.reader(f)
        next(handle)
        for line in handle:
            gene = line[1]
            description = line[2]
            gene_id = line[3]
            gene_biotype = line[4]
            dict_of_genes[gene] = line

    return dict_of_genes


def get_unique_genes(rcd, rcd_genes_master_dict, unique_genes_dir):
    all_other_genes = set()
    for rcd_type, genes in rcd_genes_master_dict.items():
        if rcd_type != rcd:
            all_other_genes = all_other_genes | set(genes)

    rcd_genes = set(rcd_genes_master_dict[rcd].keys())
    unique_genes = rcd_genes - all_other_genes

    with open(f"{unique_genes_dir}/{rcd}.csv", "w", newline="") as f:
        unique_genes_info = [
            [
                "deathtype",
                "gene",
                "description",
                "gene_id",
                "gene_biotype",
                "pmid",
                "comment",
            ]
        ]
        for gene in unique_genes:
            unique_genes_info.append(rcd_genes_master_dict[rcd][gene])

        handle = csv.writer(f)
        handle.writerows(unique_genes_info)


def main(rcd_dir, unique_genes_dir):
    os.makedirs(unique_genes_dir, exist_ok=True)

    rcd_genes_master_dict = {}
    rcd_types_of_interest = ["Necroptosis", "Pyroptosis", "Ferroptosis"]
    for rcd_file in [f"{rcd_type}.csv" for rcd_type in rcd_types_of_interest]:
        rcd_type = get_rcd_type(rcd_file)
        rcd_genes_master_dict[rcd_type] = make_dict_of_genes(f"{rcd_dir}/{rcd_file}")

    for rcd_type in rcd_types_of_interest:
        get_unique_genes(rcd_type, rcd_genes_master_dict, unique_genes_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rcd-gene-list-dir",
        help="path to the directory containing the list of RCD-related genes",
    )
    parser.add_argument(
        "--output-dir",
        help="path to the output directory that will store the unique genes per RCD type",
    )

    args = parser.parse_args()
    main(args.rcd_gene_list_dir, args.output_dir)
