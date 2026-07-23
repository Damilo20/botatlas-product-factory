"use client";

import { useMemo, useState } from "react";
import { searchProducts } from "../services/search.service";

export function useSearch(initialQuery = "") {
  const [query, setQuery] = useState(initialQuery);

  const results = useMemo(
    () => searchProducts(query),
    [query]
  );

  return {
    query,
    results,
    setQuery,
    hasResults: results.length > 0,
    isSearching: query.trim().length > 0,
  };
}