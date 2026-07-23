"use client";

import SearchBar from "@/components/search/SearchExperience";
import TrendingProducts from "@/sections/TrendingProducts";
import { useSearch } from "@/features/search/hooks/useSearch";

export default function SearchExperience() {
  const { query, setQuery } = useSearch();

  return (
    <>
      <SearchBar
        query={query}
        onChange={setQuery}
      />

      <TrendingProducts />
    </>
  );
}