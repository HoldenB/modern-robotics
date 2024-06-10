from planning.rrt import TreeNode, RRTAlgorithm


def main() -> None:
    # Testing node/rrt
    node = TreeNode(1.1, 1.1)
    rrt = RRTAlgorithm(node, node, 100, 1, 20)


if __name__ == "__main__":
    main()
