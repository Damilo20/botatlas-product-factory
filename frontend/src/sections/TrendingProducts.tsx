import ProductCard from "@/components/cards/ProductCard";
import { products } from "@/data/products";

export default function TrendingProducts() {
  return (
    <section className="mt-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {products.map((product) => (
        <ProductCard
          key={product.id}
          brand={product.brand}
          name={product.name}
          trustScore={product.trustScore}
        />
      ))}
    </section>
  );
}