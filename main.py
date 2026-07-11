from scripts.engine.product_factory import ProductFactory


def main():
    factory = ProductFactory()

    product = factory.build_product(
        "Figure AI Figure 02"
    )

    print()
    print("🧠 TESTING BOTALAS MEMORY")
    print("=" * 50)

    stored_product = factory.repository.load(
        product.product_id
    )

    if stored_product:
        print("✓ Product retrieved from memory")
        print()
        print(stored_product)
    else:
        print("✗ Product not found in memory")


if __name__ == "__main__":
    main()