
import * as React from "react"
import Image from "next/image"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export default function Home() {
  return (
    <div>
      <Image
        src="/logo.svg"
        width={500}
        height={500}
        alt="Picture of the author"
        priority
      />
      <DropdownMenu>
        <DropdownMenuTrigger className="border-2 radius-xs ml-5">Month</DropdownMenuTrigger>
        <DropdownMenuContent className="ml-5">
          <DropdownMenuItem>January</DropdownMenuItem>
          <DropdownMenuItem>February</DropdownMenuItem>
          <DropdownMenuItem>March</DropdownMenuItem>
          <DropdownMenuItem>April</DropdownMenuItem>
          <DropdownMenuItem>May</DropdownMenuItem>
          <DropdownMenuItem>June</DropdownMenuItem>
          <DropdownMenuItem>July</DropdownMenuItem>
          <DropdownMenuItem>August</DropdownMenuItem>
          <DropdownMenuItem>September</DropdownMenuItem>
          <DropdownMenuItem>October</DropdownMenuItem>
          <DropdownMenuItem>November</DropdownMenuItem>
          <DropdownMenuItem>December</DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  )
}
