import SearchExperience from "@/sections/SearchExperience";
"use client";

type Props = {
  query: string;
  onChange: (value: string) => void;
};

export default function SearchBar({
  query,
  onChange,
}: Props) {
  return (
    <input
      value={query}
      onChange={(e) => onChange(e.target.value)}
      placeholder="Search products..."
      className="w-full rounded-xl border border-neutral-700 bg-neutral-900 px-6 py-4 text-lg outline-none focus:border-blue-500"
    />
  );
}