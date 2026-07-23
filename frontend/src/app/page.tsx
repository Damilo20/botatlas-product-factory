import TrendingProducts from "@/sections/TrendingProducts";
import Hero from "@/components/home/Hero";
import SearchBar from "@/components/search/SearchExperience";

export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center px-6">

      <Hero />

      <SearchExperience />

      <TrendingProducts />

    </main>
  );
}