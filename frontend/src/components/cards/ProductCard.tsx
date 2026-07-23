type ProductCardProps = {
  brand: string;
  name: string;
  trustScore: number;
};

export default function ProductCard({
  brand,
  name,
  trustScore,
}: ProductCardProps) {
  return (
    <article className="rounded-2xl border border-neutral-800 bg-neutral-900 p-6 transition hover:border-blue-500 hover:-translate-y-1">

      <p className="text-sm uppercase tracking-wide text-gray-500">
        {brand}
      </p>

      <h2 className="mt-2 text-2xl font-bold">
        {name}
      </h2>

      <div className="mt-6 flex items-center justify-between">

        <span className="text-gray-400">
          Trust Score
        </span>

        <span className="rounded-full bg-green-500/20 px-3 py-1 font-bold text-green-400">
          {trustScore}
        </span>

      </div>

    </article>
  );
}